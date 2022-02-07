from .generate_data import QUESTIONHEADS,QUESTION,ANSWER,ADDUSERS
from legal.tables import QuestionHead,Questions,Answers,AddUser


def load_data():
    """
    Load some example data into the database.
    """
    for table_class in [QuestionHead,Questions,Answers,AddUser]:
        table_class.delete(force=True).run_sync()

    QuestionHead.insert(*[QuestionHead(**d) for d in QUESTIONHEADS]).run_sync()
    Questions.insert(*[Questions(**m) for m in QUESTION]).run_sync()
    Answers.insert(*[Answers(**s) for s in ANSWER]).run_sync()
    AddUser.insert(*[AddUser(**s) for s in  ADDUSERS]).run_sync()


    engine_type = QuestionHead._meta.db.engine_type

    if engine_type == "postgres":
        # We need to update the sequence, as we explicitly set the IDs.
        QuestionHead.raw(
            "SELECT setval('director_id_seq', max(id)) FROM director"
        ).run_sync()
        Questions.raw(
            "SELECT setval('movie_id_seq', max(id)) FROM movie"
        ).run_sync()
        Answers.raw(
            "SELECT setval('studio_id_seq', max(id)) FROM studio"
        ).run_sync()
        AddUser.raw(
            "SELECT setval('studio_id_seq', max(id)) FROM studio"
        ).run_sync()