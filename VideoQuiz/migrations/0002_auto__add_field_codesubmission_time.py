# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CodeSubmission.time'
        db.add_column(u'VideoQuiz_codesubmission', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CodeSubmission.time'
        db.delete_column(u'VideoQuiz_codesubmission', 'time')


    models = {
        u'VideoQuiz.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['VideoQuiz.Question']"})
        },
        u'VideoQuiz.code': {
            'Meta': {'object_name': 'Code'},
            'charity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'chosen_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'finished_watching': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'giftcard_amount': ('django.db.models.fields.FloatField', [], {'default': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_it_foward': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['VideoQuiz.Quiz']"}),
            'quiz_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'started_watching': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['VideoQuiz.Store']", 'null': 'True', 'blank': 'True'}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['VideoQuiz.Voter']"})
        },
        u'VideoQuiz.codesubmission': {
            'Meta': {'object_name': 'CodeSubmission'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.TextField', [], {'max_length': '20'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        },
        u'VideoQuiz.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['VideoQuiz.Quiz']"})
        },
        u'VideoQuiz.quiz': {
            'Meta': {'object_name': 'Quiz'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'VideoQuiz.quizresponse': {
            'Meta': {'object_name': 'QuizResponse'},
            'answers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['VideoQuiz.Answer']", 'symmetrical': 'False'}),
            'code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['VideoQuiz.Code']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['VideoQuiz.Quiz']"})
        },
        u'VideoQuiz.store': {
            'Meta': {'object_name': 'Store'},
            'charity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'VideoQuiz.voter': {
            'Meta': {'object_name': 'Voter'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['VideoQuiz']