from datetime import date, timedelta


class Student:
    """ 
    A Student class as a basis for method testing 
    * Create a new test method called test_apply_extension
    * Inside test_apply_extension, store the current end_date for our student_instance in a variable called old_end_date
    * Call a method named apply_extension that will take a number of days as an argument on the student instance to update the end_date
    * Assert whether the instance's end_date equals the old end date plus the days argument that was passed in using timedelta
    * In the student class, create a new method called apply_extension that has a parameter called days
    * Use the timedelta method from datetime to update the end_date property
    * Run the tests to confirm they are working 
    """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, days):
        self.end_date += timedelta(days=days)