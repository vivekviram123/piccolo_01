import enum
from unicodedata import name
from piccolo.table import Table
from piccolo.table import Readable
from piccolo.columns import Varchar,Text,Array,ForeignKey
from piccolo.columns.reference import LazyTableReference




class QuestionHead(Table):
    
    name = Varchar(length=300,null=False)
    


class Questions(Table):
    
    class QuestionType(enum.Enum):
        dropdown = "dropdown"
        checkbox ="checkbox"

        input ="input"

    # question_head = ForeignKey(references=LazyTableReference(
    #        table_class_name="QuestionHead",module_path="legal.tables"))
    question_head = ForeignKey(references=QuestionHead)
    question = Text()
    option = Array(base_column=Varchar())
    question_type = Varchar(length=20, choices=QuestionType)


class Answers(Table):

    question = ForeignKey(Questions)
    answer = Text()
    


class AddUser(Table):

    name  = Varchar()
    contact_no = Varchar()
    email = Varchar()
    address = Text()
    
