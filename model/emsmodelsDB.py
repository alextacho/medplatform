from google.appengine.ext import db

class SubTestKategory(db.Model):
	name = db.StringProperty()


class BasicUnderstanding(db.Model):
	description = db.StringProperty(required=True)
	answer1 = db.ReferenceProperty(Answer)
	answer2 = db.ReferenceProperty(Answer)
	answer3 = db.ReferenceProperty(Answer)
	answer4 = db.ReferenceProperty(Answer)
	answer5 = db.ReferenceProperty(Answer)
	

class Answer(db.Model):
	text = db.StringPropety()
	isRight = db.BooleanProperty()



