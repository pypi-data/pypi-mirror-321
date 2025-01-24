"""
Security analysis module for keystroke patterns and threat detection.
"""

import json
import time
import hashlib
import statistics
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from collections import defaultdict
import numpy as np
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class KeystrokeSecurityAnalyzer:
    """Analyzes keystroke patterns for security purposes."""
    
    def __init__(self, encryption_key: Optional[str] = None):
        """Initialize the security analyzer.
        
        Args:
            encryption_key: Optional key for encrypting logged data
        """
        self.typing_patterns = defaultdict(list)
        self.key_sequences = []
        self.timing_data = []
        self.suspicious_patterns = []
        self.baseline_profile = None
        
        # Set up encryption
        if encryption_key:
            self.setup_encryption(encryption_key)
        else:
            self.fernet = None
            
    def setup_encryption(self, key: str):
        """Set up encryption for sensitive data."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'keystroke_security',
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(key.encode()))
        self.fernet = Fernet(key)
        
    def analyze_keystroke_dynamics(self, 
                                 key_data: List[Dict],
                                 window_size: int = 100) -> Dict:
        """Analyze keystroke dynamics for authentication.
        
        Args:
            key_data: List of keystroke events with timing
            window_size: Size of analysis window
            
        Returns:
            Dictionary containing analysis results
        """
        results = {
            'timing_patterns': [],
            'rhythm_consistency': 0.0,
            'anomaly_score': 0.0,
            'potential_threats': []
        }
        
        # Extract timing patterns
        for i in range(len(key_data) - 1):
            current = key_data[i]
            next_key = key_data[i + 1]
            
            # Calculate key hold time
            hold_time = current['release_time'] - current['press_time']
            
            # Calculate flight time between keys
            flight_time = next_key['press_time'] - current['release_time']
            
            results['timing_patterns'].append({
                'key_pair': f"{current['key']}-{next_key['key']}",
                'hold_time': hold_time,
                'flight_time': flight_time
            })
            
        # Analyze rhythm consistency
        if len(results['timing_patterns']) > 1:
            hold_times = [p['hold_time'] for p in results['timing_patterns']]
            flight_times = [p['flight_time'] for p in results['timing_patterns']]
            
            hold_std = statistics.stdev(hold_times) if len(hold_times) > 1 else 0
            flight_std = statistics.stdev(flight_times) if len(flight_times) > 1 else 0
            
            results['rhythm_consistency'] = 1.0 / (1.0 + hold_std + flight_std)
            
        # Detect anomalies
        if self.baseline_profile:
            anomaly_score = self._calculate_anomaly_score(results['timing_patterns'])
            results['anomaly_score'] = anomaly_score
            
            if anomaly_score > 0.7:  # Threshold for suspicious activity
                results['potential_threats'].append({
                    'type': 'anomalous_typing_pattern',
                    'score': anomaly_score,
                    'timestamp': datetime.now().isoformat()
                })
                
        return results
        
    def create_baseline_profile(self, training_data: List[Dict]):
        """Create baseline user profile from training data."""
        profile = {
            'key_frequencies': defaultdict(int),
            'timing_patterns': defaultdict(list),
            'common_sequences': defaultdict(int)
        }
        
        # Analyze training data
        for event in training_data:
            key = event['key']
            profile['key_frequencies'][key] += 1
            
            # Record timing patterns
            if len(self.timing_data) > 0:
                last_event = self.timing_data[-1]
                pair = f"{last_event['key']}-{key}"
                timing = event['timestamp'] - last_event['timestamp']
                profile['timing_patterns'][pair].append(timing)
            
            self.timing_data.append(event)
            
            # Analyze sequences
            self.key_sequences.append(key)
            if len(self.key_sequences) >= 3:
                seq = ''.join(self.key_sequences[-3:])
                profile['common_sequences'][seq] += 1
                
        # Calculate statistics
        self.baseline_profile = {
            'key_frequencies': dict(profile['key_frequencies']),
            'timing_means': {
                pair: statistics.mean(times)
                for pair, times in profile['timing_patterns'].items()
                if len(times) > 1
            },
            'timing_stdevs': {
                pair: statistics.stdev(times)
                for pair, times in profile['timing_patterns'].items()
                if len(times) > 1
            },
            'common_sequences': dict(
                sorted(
                    profile['common_sequences'].items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:100]  # Keep top 100 sequences
            )
        }
        
    def detect_threats(self, 
                      current_data: List[Dict], 
                      sensitivity: float = 0.7) -> List[Dict]:
        """Detect potential security threats from keystroke patterns.
        
        Args:
            current_data: Recent keystroke data
            sensitivity: Detection sensitivity (0-1)
            
        Returns:
            List of detected threats
        """
        threats = []
        
        # Analyze typing rhythm
        rhythm_analysis = self.analyze_keystroke_dynamics(current_data)
        if rhythm_analysis['anomaly_score'] > sensitivity:
            threats.append({
                'type': 'unusual_typing_pattern',
                'severity': 'medium',
                'details': {
                    'anomaly_score': rhythm_analysis['anomaly_score'],
                    'timestamp': datetime.now().isoformat()
                }
            })
            
        # Check for rapid input
        if self._detect_rapid_input(current_data):
            threats.append({
                'type': 'rapid_input',
                'severity': 'high',
                'details': 'Unusually fast typing detected - possible automated input'
            })
            
        # Look for suspicious sequences
        suspicious_seqs = self._detect_suspicious_sequences(current_data)
        if suspicious_seqs:
            threats.append({
                'type': 'suspicious_sequence',
                'severity': 'high',
                'details': {
                    'sequences': suspicious_seqs,
                    'timestamp': datetime.now().isoformat()
                }
            })
            
        return threats
        
    def _calculate_anomaly_score(self, 
                               patterns: List[Dict]) -> float:
        """Calculate anomaly score based on deviation from baseline."""
        if not self.baseline_profile or not patterns:
            return 0.0
            
        deviations = []
        for pattern in patterns:
            pair = pattern['key_pair']
            if pair in self.baseline_profile['timing_means']:
                baseline_mean = self.baseline_profile['timing_means'][pair]
                baseline_std = self.baseline_profile['timing_stdevs'][pair]
                
                # Calculate z-score
                hold_zscore = abs(
                    (pattern['hold_time'] - baseline_mean) / 
                    (baseline_std if baseline_std > 0 else 1)
                )
                deviations.append(hold_zscore)
                
        return statistics.mean(deviations) if deviations else 0.0
        
    def _detect_rapid_input(self, 
                          data: List[Dict], 
                          threshold: float = 0.05) -> bool:
        """Detect unusually rapid keyboard input."""
        if len(data) < 2:
            return False
            
        intervals = []
        for i in range(len(data) - 1):
            interval = data[i + 1]['timestamp'] - data[i]['timestamp']
            intervals.append(interval)
            
        avg_interval = statistics.mean(intervals)
        return avg_interval < threshold
        
    def _detect_suspicious_sequences(self, 
                                   data: List[Dict], 
                                   min_length: int = 3) -> List[str]:
        """Detect potentially suspicious key sequences."""
        suspicious = []
        sequence = ''.join(event['key'] for event in data)
        
        # Check for repeated sequences
        for i in range(len(sequence) - min_length + 1):
            substr = sequence[i:i + min_length]
            if sequence.count(substr) > 3:  # Threshold for repetition
                suspicious.append(substr)
                
        # Check for known malicious patterns
        malicious_patterns = [
            'sudo', 'chmod', 'rm -rf', 'wget', 'curl',
            ';bash', '&&bash', '||bash', '${IFS}', '>/dev/null'
        ]
        
        for pattern in malicious_patterns:
            if pattern in sequence:
                suspicious.append(pattern)
                
        return list(set(suspicious))  # Remove duplicates
        
    def encrypt_log_data(self, data: Dict) -> bytes:
        """Encrypt sensitive log data."""
        if not self.fernet:
            raise ValueError("Encryption not initialized")
            
        return self.fernet.encrypt(json.dumps(data).encode())
        
    def decrypt_log_data(self, encrypted_data: bytes) -> Dict:
        """Decrypt encrypted log data."""
        if not self.fernet:
            raise ValueError("Encryption not initialized")
            
        decrypted = self.fernet.decrypt(encrypted_data)
        return json.loads(decrypted.decode())
        
    def generate_security_report(self, 
                               data: List[Dict],
                               include_timing: bool = True) -> Dict:
        """Generate comprehensive security analysis report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'analysis_period': {
                'start': data[0]['timestamp'] if data else None,
                'end': data[-1]['timestamp'] if data else None
            },
            'threats_detected': self.detect_threats(data),
            'statistics': {
                'total_keystrokes': len(data),
                'unique_keys': len(set(d['key'] for d in data)),
                'suspicious_patterns': len(self.suspicious_patterns)
            }
        }
        
        if include_timing:
            rhythm_analysis = self.analyze_keystroke_dynamics(data)
            report['timing_analysis'] = {
                'rhythm_consistency': rhythm_analysis['rhythm_consistency'],
                'anomaly_score': rhythm_analysis['anomaly_score']
            }
            
        # Calculate risk score
        risk_factors = [
            len(report['threats_detected']) * 0.4,
            (rhythm_analysis['anomaly_score'] if include_timing else 0) * 0.3,
            (len(self.suspicious_patterns) / max(len(data), 1)) * 0.3
        ]
        report['risk_score'] = sum(risk_factors)
        
        return report
