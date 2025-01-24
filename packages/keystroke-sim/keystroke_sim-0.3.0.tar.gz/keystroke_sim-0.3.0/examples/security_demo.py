"""
Demonstration of KeystrokeSimulator's security features.
"""

import time
import json
from datetime import datetime
from keystroke_sim import KeyboardMonitor
from keystroke_sim.security_analyzer import KeystrokeSecurityAnalyzer

def create_training_data(monitor: KeyboardMonitor, duration: int = 30):
    """Collect training data for user profiling."""
    print("\n=== Collecting Training Data ===")
    print(f"Please type normally for {duration} seconds to create your baseline profile...")
    print("This will be used to detect anomalies later.")
    
    training_data = []
    start_time = time.time()
    
    def collect_data(event):
        if event.event_type == 'down':
            training_data.append({
                'key': event.name,
                'press_time': time.time(),
                'release_time': None,
                'timestamp': datetime.now().timestamp()
            })
        elif event.event_type == 'up' and training_data:
            # Update the release time of the last matching key press
            for entry in reversed(training_data):
                if entry['key'] == event.name and entry['release_time'] is None:
                    entry['release_time'] = time.time()
                    break
    
    monitor.on_event = collect_data
    monitor.start()
    
    try:
        while time.time() - start_time < duration:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        monitor.stop()
        
    # Remove incomplete entries
    training_data = [d for d in training_data if d['release_time'] is not None]
    return training_data

def monitor_with_security(analyzer: KeystrokeSecurityAnalyzer, 
                         monitor: KeyboardMonitor,
                         alert_threshold: float = 0.7):
    """Monitor keyboard input with security analysis."""
    print("\n=== Security Monitoring Started ===")
    print("Now monitoring for suspicious activity...")
    print("Press Ctrl+C to stop")
    
    current_data = []
    last_report_time = time.time()
    report_interval = 10  # Generate report every 10 seconds
    
    def security_callback(event):
        if event.event_type == 'down':
            current_data.append({
                'key': event.name,
                'press_time': time.time(),
                'release_time': None,
                'timestamp': datetime.now().timestamp()
            })
        elif event.event_type == 'up' and current_data:
            # Update release time
            for entry in reversed(current_data):
                if entry['key'] == event.name and entry['release_time'] is None:
                    entry['release_time'] = time.time()
                    break
                    
            # Generate periodic security reports
            nonlocal last_report_time
            if time.time() - last_report_time >= report_interval:
                report = analyzer.generate_security_report(current_data)
                display_security_report(report)
                last_report_time = time.time()
                
                # Alert on high risk score
                if report['risk_score'] > alert_threshold:
                    display_security_alert(report)
                
                # Save report
                save_security_report(report)
                
                # Clear old data while keeping recent entries
                current_data = current_data[-100:]  # Keep last 100 events
    
    monitor.on_event = security_callback
    monitor.start()
    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        monitor.stop()
        
def display_security_report(report: dict):
    """Display security analysis report."""
    print("\n=== Security Report ===")
    print(f"Timestamp: {report['timestamp']}")
    print(f"Risk Score: {report['risk_score']:.2f}")
    
    if report['threats_detected']:
        print("\nThreats Detected:")
        for threat in report['threats_detected']:
            print(f"- {threat['type']} (Severity: {threat['severity']})")
            if isinstance(threat['details'], dict):
                for key, value in threat['details'].items():
                    print(f"  {key}: {value}")
            else:
                print(f"  Details: {threat['details']}")
    
    print("\nStatistics:")
    for key, value in report['statistics'].items():
        print(f"- {key}: {value}")
        
    if 'timing_analysis' in report:
        print("\nTiming Analysis:")
        print(f"- Rhythm Consistency: {report['timing_analysis']['rhythm_consistency']:.2f}")
        print(f"- Anomaly Score: {report['timing_analysis']['anomaly_score']:.2f}")

def display_security_alert(report: dict):
    """Display security alert for high-risk activities."""
    print("\n!!! SECURITY ALERT !!!")
    print(f"High risk activity detected (Score: {report['risk_score']:.2f})")
    
    if report['threats_detected']:
        print("\nDetected Threats:")
        for threat in report['threats_detected']:
            print(f"- {threat['type']} ({threat['severity'].upper()})")
            
    print("\nRecommended Actions:")
    if any(t['severity'] == 'high' for t in report['threats_detected']):
        print("- Investigate immediately")
        print("- Consider terminating suspicious processes")
        print("- Review system logs")
    else:
        print("- Monitor situation")
        print("- Review recent activity")

def save_security_report(report: dict, filename: str = "security_report.json"):
    """Save security report to file."""
    try:
        # Load existing reports
        try:
            with open(filename, 'r') as f:
                reports = json.load(f)
        except FileNotFoundError:
            reports = []
            
        # Add new report
        reports.append(report)
        
        # Keep only last 100 reports
        reports = reports[-100:]
        
        # Save updated reports
        with open(filename, 'w') as f:
            json.dump(reports, f, indent=2)
    except Exception as e:
        print(f"Error saving report: {e}")

def main():
    print("=== KeystrokeSimulator Security Demo ===")
    print("\nThis demo will:")
    print("1. Collect training data to create your typing profile")
    print("2. Monitor keyboard input for security threats")
    print("3. Generate security reports and alerts")
    
    # Initialize components
    monitor = KeyboardMonitor()
    analyzer = KeystrokeSecurityAnalyzer(encryption_key="demo-security-key")
    
    # Collect training data
    training_data = create_training_data(monitor)
    
    # Create baseline profile
    print("\nCreating baseline profile...")
    analyzer.create_baseline_profile(training_data)
    print("Baseline profile created!")
    
    # Start security monitoring
    monitor_with_security(analyzer, monitor)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDemo stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
