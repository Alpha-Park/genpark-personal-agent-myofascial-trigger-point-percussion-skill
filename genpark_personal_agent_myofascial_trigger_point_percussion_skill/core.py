# -*- coding: utf-8 -*-
"""Myofascial Trigger Point Percussion Coach for GenPark Personal Agent."""
import json
from typing import Dict, Any

class MyofascialTriggerPointPercussionCoach:
    @staticmethod
    def prescribe_percussion_therapy_protocol(target_muscle_group: str, muscle_tightness_level: str = "moderate") -> Dict[str, Any]:
        muscle = target_muscle_group.lower()
        if "quad" in muscle or "glute" in muscle or "hamstring" in muscle:
            head = "Large Round Foam Ball"
            speed = "30 Hz (1800 RPM) for deep tissue penetration"
            duration = 120
        elif "neck" in muscle or "trap" in muscle:
            head = "Dampener Soft Head"
            speed = "20 Hz (1200 RPM) low vibration to protect cervical nerves"
            duration = 60
        else:
            head = "Standard Bullet or Flat Head"
            speed = "25 Hz (1500 RPM)"
            duration = 90
            
        return {
            "muscle_group": target_muscle_group,
            "recommended_attachment": head,
            "frequency_calibration": speed,
            "treatment_duration_seconds": duration,
            "technique_guideline": "Float device gently along muscle fiber orientation; never press forcefully onto bony landmarks."
        }

    @staticmethod
    def calculate_ischemic_compression_countdown(trigger_point_depth: str, pain_threshold_scale_10: int = 5) -> Dict[str, Any]:
        seconds = 90 if trigger_point_depth == "deep" else 60
        return {
            "target_depth": trigger_point_depth,
            "prescribed_hold_seconds": seconds,
            "pressure_target": "Maintain pain intensity at strictly 5-6 out of 10 (discomfort, not sharp guarding)",
            "mechanism": "Induces reactive hyperemia: transient ischemia followed by surge of oxygenated blood upon release."
        }
