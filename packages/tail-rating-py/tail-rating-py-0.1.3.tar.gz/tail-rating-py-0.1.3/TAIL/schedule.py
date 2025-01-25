from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import date, datetime, time, timedelta
import holidays
import pandas as pd


# Define the model for a period within a day
class Period(BaseModel):
    start_time: str  # e.g., '08:00'
    end_time: str  # e.g., '10:00'
    intensity: float  # Intensity of the activity (0 to 1)
    intensity_number: Optional[int] = 1  # Optional field for intensity number (default is 1)

    @field_validator("intensity")
    def check_intensity(cls, intensity):
        if not (0 <= intensity <= 1):
            raise ValueError("Intensity must be between 0 and 1")
        return intensity


# Define the model for a single day schedule
class DaySchedule(BaseModel):
    day_of_week: int  # 0=Monday, 1=Tuesday, ..., 6=Sunday
    period_list: List[Period]  # List of periods for that day


# Define the model for weekly schedules
class WeekSchedule(BaseModel):
    week_number: int  # Week number in the year (1-52)
    days: List[DaySchedule]  # List of day schedules for that week


# Define the model for holiday periods
class HolidayPeriod(BaseModel):
    start_date: date  # Start date of the holiday
    end_date: date  # End date of the holiday
    holiday_name: str  # Name of the holiday (e.g., 'Christmas')


# Define the main model that holds the entire yearly schedule
class YearSchedule(BaseModel):
    year: int  # The year the schedule applies to
    weekly_schedules: List[WeekSchedule]  # Weekly schedules
    holiday_periods: List[HolidayPeriod]  # List of holiday periods
    additional_notes: Optional[str] = None  # Optional field for any extra notes
    include_public_holidays: bool = False  # Flag to include public holidays
    public_holiday_country: Optional[str] = None  # Country code for public holidays

    @field_validator("year")
    def check_year(cls, year):
        if year < 1000 or year > 9999:
            raise ValueError("Year must be a valid 4-digit year")
        return year

    def add_public_holidays(self):
        if self.include_public_holidays and self.public_holiday_country:
            country_holidays = holidays.CountryHoliday(self.public_holiday_country, years=self.year)
            for holiday_date, holiday_name in country_holidays.items():
                self.holiday_periods.append(
                    HolidayPeriod(start_date=holiday_date, end_date=holiday_date, holiday_name=holiday_name)
                )


def convert_to_series(schedule: YearSchedule) -> pd.Series:
    start_date = pd.Timestamp(f"{schedule.year}-01-01")
    end_date = pd.Timestamp(f"{schedule.year}-12-31")
    index = pd.date_range(start=start_date, end=end_date, freq="15min")
    series = pd.Series(data=0.0, index=index)

    for week_schedule in schedule.weekly_schedules:
        for day_schedule in week_schedule.days:
            for period in day_schedule.period_list:
                week_start = start_date + timedelta(weeks=week_schedule.week_number - 1)
                day_date = week_start + timedelta(days=day_schedule.day_of_week)
                start_time = datetime.combine(day_date, datetime.strptime(period.start_time, "%H:%M").time())
                end_time = datetime.combine(day_date, datetime.strptime(period.end_time, "%H:%M").time())
                series[start_time:end_time] = period.intensity

    for holiday_period in schedule.holiday_periods:
        series[holiday_period.start_date:holiday_period.end_date] = 0.0

    return series


def create_basic_schedule(year: int, country: str = "DK") -> YearSchedule:
    schedule = YearSchedule(year=year, weekly_schedules=[], holiday_periods=[], include_public_holidays=True, public_holiday_country=country)
    schedule.add_public_holidays()

    day_schedule = [DaySchedule(day_of_week=day, period_list=[Period(start_time="08:00", end_time="17:00", intensity=1)]) for day in range(5)]
    for week_number in range(1, 53):
        schedule.weekly_schedules.append(WeekSchedule(week_number=week_number, days=day_schedule))

    return schedule


schedule = create_basic_schedule(2025)
series = convert_to_series(schedule)
