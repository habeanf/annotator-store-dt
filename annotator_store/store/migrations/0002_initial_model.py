# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Annotation'
        db.create_table('store_annotation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('quote', self.gf('django.db.models.fields.TextField')()),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='annotations', to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('consumer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', blank=True, to=orm['store.Annotation'])),
        ))
        db.send_create_signal('store', ['Annotation'])

        # Adding model 'Range'
        db.create_table('store_range', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('annotation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ranges', to=orm['store.Annotation'])),
            ('start', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('end', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('startOffset', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('endOffset', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('store', ['Range'])

        # Adding model 'Permission'
        db.create_table('store_permission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('annotation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permissions', to=orm['store.Annotation'])),
        ))
        db.send_create_signal('store', ['Permission'])

        # Adding M2M table for field read on 'Permission'
        db.create_table('store_permission_read', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('permission', models.ForeignKey(orm['store.permission'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('store_permission_read', ['permission_id', 'user_id'])

        # Adding M2M table for field update on 'Permission'
        db.create_table('store_permission_update', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('permission', models.ForeignKey(orm['store.permission'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('store_permission_update', ['permission_id', 'user_id'])

        # Adding M2M table for field delete on 'Permission'
        db.create_table('store_permission_delete', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('permission', models.ForeignKey(orm['store.permission'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('store_permission_delete', ['permission_id', 'user_id'])

        # Adding M2M table for field admin on 'Permission'
        db.create_table('store_permission_admin', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('permission', models.ForeignKey(orm['store.permission'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('store_permission_admin', ['permission_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'Annotation'
        db.delete_table('store_annotation')

        # Deleting model 'Range'
        db.delete_table('store_range')

        # Deleting model 'Permission'
        db.delete_table('store_permission')

        # Removing M2M table for field read on 'Permission'
        db.delete_table('store_permission_read')

        # Removing M2M table for field update on 'Permission'
        db.delete_table('store_permission_update')

        # Removing M2M table for field delete on 'Permission'
        db.delete_table('store_permission_delete')

        # Removing M2M table for field admin on 'Permission'
        db.delete_table('store_permission_admin')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'store.annotation': {
            'Meta': {'object_name': 'Annotation'},
            'consumer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'blank': 'True', 'to': "orm['store.Annotation']"}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'annotations'", 'to': "orm['auth.User']"})
        },
        'store.permission': {
            'Meta': {'object_name': 'Permission'},
            'admin': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'annotation_admin_permissions'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'annotation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'to': "orm['store.Annotation']"}),
            'delete': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'annotation_delete_permissions'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'annotation_read_permissions'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'update': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'annotation_update_permissions'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'store.range': {
            'Meta': {'object_name': 'Range'},
            'annotation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ranges'", 'to': "orm['store.Annotation']"}),
            'end': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'endOffset': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'startOffset': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['store']