"""
Flexible date/time parsing service
"""
from datetime import datetime, timedelta
from typing import Optional
import dateutil.parser


def parse_flexible_date(date_string: str) -> Optional[datetime]:
    """
    Parses a flexible date string into a datetime object.
    Supports formats like "tomorrow 3pm", "next monday 9:00", "in 2 hours", etc.

    Args:
        date_string: The date string to parse

    Returns:
        The parsed datetime object, or None if parsing fails
    """
    if not date_string or not date_string.strip():
        return None

    try:
        # Try to parse the date string using dateutil.parser
        parsed_date = dateutil.parser.parse(date_string, fuzzy=True)
        return parsed_date
    except (ValueError, TypeError, dateutil.parser.ParserError):
        # If dateutil fails, try some common patterns manually
        date_string = date_string.strip().lower()
        
        # Handle "in X hours/minutes/days" patterns
        if date_string.startswith("in "):
            try:
                parts = date_string.split()
                if len(parts) >= 3 and parts[2] in ["hour", "hours", "minute", "minutes", "day", "days"]:
                    value = int(parts[1])
                    now = datetime.now()
                    
                    if parts[2] in ["hour", "hours"]:
                        return now + timedelta(hours=value)
                    elif parts[2] in ["minute", "minutes"]:
                        return now + timedelta(minutes=value)
                    elif parts[2] in ["day", "days"]:
                        return now + timedelta(days=value)
            except (ValueError, IndexError):
                pass
        
        # Handle "tomorrow" patterns
        if date_string.startswith("tomorrow"):
            tomorrow = datetime.now().date() + timedelta(days=1)
            time_part = "00:00"
            
            # Extract time if provided (e.g., "tomorrow 3pm")
            time_portion = date_string.replace("tomorrow", "").strip()
            if time_portion:
                # Simple time parsing for common formats
                if "pm" in time_portion or "am" in time_portion:
                    # Handle 12-hour format
                    time_part = time_portion.replace("pm", "").replace("am", "").strip()
                    hour_min = time_part.split(":")
                    hour = int(hour_min[0])
                    minute = int(hour_min[1]) if len(hour_min) > 1 else 0
                    
                    if "pm" in time_portion and hour != 12:
                        hour += 12
                    elif "am" in time_portion and hour == 12:
                        hour = 0
                        
                    return datetime.combine(tomorrow, datetime.min.time().replace(hour=hour, minute=minute))
                else:
                    # Handle 24-hour format
                    return datetime.combine(tomorrow, datetime.min.time().replace(hour=int(time_portion.split(":")[0]), minute=int(time_portion.split(":")[1]) if ":" in time_portion else 0))
            else:
                return datetime.combine(tomorrow, datetime.min.time())
        
        # Handle "next [day]" patterns
        if date_string.startswith("next "):
            day_name = date_string.replace("next ", "").split()[0]
            today = datetime.now()
            
            # Map day names to numbers (Monday=0, Sunday=6)
            days = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, 
                   "friday": 4, "saturday": 5, "sunday": 6}
            
            if day_name in days:
                target_day = days[day_name]
                current_day = today.weekday()
                
                # Calculate days until next occurrence
                days_ahead = target_day - current_day
                if days_ahead <= 0:  # Target day already happened this week
                    days_ahead += 7
                
                next_date = today.date() + timedelta(days=days_ahead)
                
                # Extract time if provided
                time_part = date_string[len(f"next {day_name}"):].strip()
                if time_part and time_part not in ["", "at"]:
                    # Simple time parsing for common formats
                    if "pm" in time_part or "am" in time_part:
                        # Handle 12-hour format
                        time_str = time_part.replace("pm", "").replace("am", "").strip()
                        hour_min = time_str.split(":")
                        hour = int(hour_min[0])
                        minute = int(hour_min[1]) if len(hour_min) > 1 else 0
                        
                        if "pm" in time_part and hour != 12:
                            hour += 12
                        elif "am" in time_part and hour == 12:
                            hour = 0
                            
                        return datetime.combine(next_date, datetime.min.time().replace(hour=hour, minute=minute))
                    else:
                        # Handle 24-hour format
                        time_parts = time_part.split(":")
                        if len(time_parts) >= 2:
                            return datetime.combine(next_date, datetime.min.time().replace(hour=int(time_parts[0]), minute=int(time_parts[1])))
                
                return datetime.combine(next_date, datetime.min.time())
        
        return None  # If all parsing attempts fail


def validate_date_format(date_string: str) -> bool:
    """
    Validates if a date string can be parsed into a valid datetime.
    
    Args:
        date_string: The date string to validate
        
    Returns:
        True if the date string is valid, False otherwise
    """
    try:
        parsed_date = parse_flexible_date(date_string)
        return parsed_date is not None
    except:
        return False