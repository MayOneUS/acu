# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Voter'
        db.create_table(u'VideoQuiz_voter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'VideoQuiz', ['Voter'])

        # Adding model 'Quiz'
        db.create_table(u'VideoQuiz_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'VideoQuiz', ['Quiz'])

        # Adding model 'Store'
        db.create_table(u'VideoQuiz_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('charity', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'VideoQuiz', ['Store'])

        # Adding model 'Code'
        db.create_table(u'VideoQuiz_code', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('voter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['VideoQuiz.Voter'])),
            ('started_watching', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('finished_watching', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['VideoQuiz.Quiz'])),
            ('quiz_complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('chosen_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['VideoQuiz.Store'], null=True, blank=True)),
            ('charity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pay_it_foward', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('giftcard_amount', self.gf('django.db.models.fields.FloatField')(default=10)),
        ))
        db.send_create_signal(u'VideoQuiz', ['Code'])

        # Adding model 'Question'
        db.create_table(u'VideoQuiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['VideoQuiz.Quiz'])),
        ))
        db.send_create_signal(u'VideoQuiz', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'VideoQuiz_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['VideoQuiz.Question'])),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'VideoQuiz', ['Answer'])

        # Adding model 'QuizResponse'
        db.create_table(u'VideoQuiz_quizresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['VideoQuiz.Code'])),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['VideoQuiz.Quiz'])),
        ))
        db.send_create_signal(u'VideoQuiz', ['QuizResponse'])

        # Adding M2M table for field answers on 'QuizResponse'
        m2m_table_name = db.shorten_name(u'VideoQuiz_quizresponse_answers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quizresponse', models.ForeignKey(orm[u'VideoQuiz.quizresponse'], null=False)),
            ('answer', models.ForeignKey(orm[u'VideoQuiz.answer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quizresponse_id', 'answer_id'])

        # Adding model 'CodeSubmission'
        db.create_table(u'VideoQuiz_codesubmission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('ip_address', self.gf('django.db.models.fields.TextField')(max_length=20)),
        ))
        db.send_create_signal(u'VideoQuiz', ['CodeSubmission'])


    def backwards(self, orm):
        # Deleting model 'Voter'
        db.delete_table(u'VideoQuiz_voter')

        # Deleting model 'Quiz'
        db.delete_table(u'VideoQuiz_quiz')

        # Deleting model 'Store'
        db.delete_table(u'VideoQuiz_store')

        # Deleting model 'Code'
        db.delete_table(u'VideoQuiz_code')

        # Deleting model 'Question'
        db.delete_table(u'VideoQuiz_question')

        # Deleting model 'Answer'
        db.delete_table(u'VideoQuiz_answer')

        # Deleting model 'QuizResponse'
        db.delete_table(u'VideoQuiz_quizresponse')

        # Removing M2M table for field answers on 'QuizResponse'
        db.delete_table(db.shorten_name(u'VideoQuiz_quizresponse_answers'))

        # Deleting model 'CodeSubmission'
        db.delete_table(u'VideoQuiz_codesubmission')


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