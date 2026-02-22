import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from gradeCalculator import GradeCalculator

class TestGradeCalculator:
    @pytest.fixture
    def calc(self): return GradeCalculator()

    def test_no_grades_returns_zero(self, calc):
        avg = calc.get_student_average(3)  # Charlie has no grades
        assert avg == 0.0, f"Expected 0.0 for no grades, got {avg}"

    def test_letter_grade_boundary(self, calc):
        assert calc.get_letter_grade(90) == 'A', "90 should be A"
        assert calc.get_letter_grade(80) == 'B', "80 should be B"

    def test_weighted_gpa(self, calc):
        gpa = calc.get_gpa(1)  # Alice: Math(4cr,92) + English(3cr,88)
        expected = (92*4 + 88*3) / (4+3)  # = 90.29
        assert abs(gpa - expected) < 0.01, f"GPA should be weighted: {expected}, got {gpa}"

    def test_rank_descending(self, calc):
        ranks = calc.get_class_rank()
        assert ranks[0]['gpa'] >= ranks[-1]['gpa'], "Rank should be highest GPA first"
