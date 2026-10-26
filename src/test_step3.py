from src.dataset import make_students
from src.practice import (
    t3_1_count_missing,
    t3_2_math_numeric,
    t3_3_remove_duplicates,
    t3_4_fill_english_median,
    t3_5_rows_after_dropna,
    t3_6_section_category,
    t3_7_clean_students,
)

df = make_students()

print("3.1 Missing values:", t3_1_count_missing(df))
print("3.2 Numeric math:", t3_2_math_numeric(df))
print("3.3 Shape after removing duplicates:", t3_3_remove_duplicates(df))
print("3.4 English after filling:", t3_4_fill_english_median(df))
print("3.5 Rows after dropna:", t3_5_rows_after_dropna(df))
print("3.6 Section dtype:", t3_6_section_category(df))
print("3.7 Cleaned students:")
print(t3_7_clean_students(df))
