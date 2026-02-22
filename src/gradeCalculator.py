import sqlite3
from typing import Dict, List

class GradeCalculator:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.row_factory = sqlite3.Row
        self._setup()

    def _setup(self):
        self.conn.executescript('''
            CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT);
            CREATE TABLE grades (
                student_id INTEGER, course TEXT, credits INTEGER,
                score DECIMAL, FOREIGN KEY(student_id) REFERENCES students(id)
            );
            INSERT INTO students VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
            INSERT INTO grades VALUES (1, 'Math', 4, 92);
            INSERT INTO grades VALUES (1, 'English', 3, 88);
            INSERT INTO grades VALUES (2, 'Math', 4, 75);
            INSERT INTO grades VALUES (2, 'English', 3, 82);
        ''')

    def get_student_average(self, student_id: int) -> float:
        # Should use COALESCE(AVG(score), 0)
        row = self.conn.execute(
            'SELECT AVG(score) as avg FROM grades WHERE student_id = ?',
            (student_id,)
        ).fetchone()
        return row['avg']

    def get_letter_grade(self, score: float) -> str:
        # 90.0 should be 'A' but gets 'B' because 90 > 90 is False
        if score > 90: return 'A'
        if score > 80: return 'B'
        if score > 70: return 'C'
        if score > 60: return 'D'
        return 'F'

    def get_gpa(self, student_id: int) -> float:
        rows = self.conn.execute(
            'SELECT credits, score FROM grades WHERE student_id = ?',
            (student_id,)
        ).fetchall()
        if not rows: return 0.0
        # Should be: sum(score * credits) / sum(credits)
        total = sum(r['score'] for r in rows)
        return round(total / len(rows), 2)

    def get_class_rank(self) -> List[Dict]:
        students = self.conn.execute('SELECT id, name FROM students').fetchall()
        ranks = []
        for s in students:
            gpa = self.get_gpa(s['id'])
            ranks.append({'name': s['name'], 'gpa': gpa})
        ranks.sort(key=lambda x: x['gpa'])
        return ranks
