# skleernexample

مكتبة بايثون لحفظ وإدارة أمثلة أكواد scikit-learn
A Python library for storing and managing scikit-learn code examples.

## التثبيت | Installation

```bash
pip install skleernexample
```

## الأمثلة الجاهزة | Built-in Examples

المكتبة تحتوي على الأمثلة الجاهزة التالية:
The library comes with the following built-in examples:

1. `decision_tree` - شجرة القرار | Decision Tree
2. `random_forest` - الغابة العشوائية | Random Forest
3. `preprocessing` - معالجة البيانات | Data Preprocessing
4. `cross_validation` - التحقق المتقاطع | Cross Validation
5. `grid_search` - البحث الشبكي | Grid Search

### كيفية استخدام الأمثلة الجاهزة | How to Use Built-in Examples

```python
from skleernexample import print_code

# عرض مثال شجرة القرار
# Display decision tree example
print_code("decision_tree")

# عرض مثال معالجة البيانات
# Display preprocessing example
print_code("preprocessing")
```

## إضافة أمثلة جديدة | Adding New Examples

```python
from skleernexample import CodeExample

# إنشاء كائن جديد
# Create new instance
code = CodeExample()

# حفظ كود جديد
# Save new code
code.save_code("my_example", """
your code here
""")
