# Generated by Django 2.2.4 on 2020-04-20 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0054_auto_20200414_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='clrmatch',
            name='comments',
            field=models.TextField(blank=True, default='', help_text='The comments.'),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='payout_contribution',
            field=models.ForeignKey(help_text='Contribution for the payout', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clr_match_payouts', to='grants.Contribution'),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='payout_tx',
            field=models.CharField(blank=True, help_text='The test payout txid', max_length=255),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='payout_tx_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='ready_for_payout',
            field=models.BooleanField(default=False, help_text='Ready for regular payout or not'),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='ready_for_test_payout',
            field=models.BooleanField(default=False, help_text='Ready for test payout or not'),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='test_payout_contribution',
            field=models.ForeignKey(help_text='Contribution for the test payout', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_clr_match_payouts', to='grants.Contribution'),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='test_payout_tx',
            field=models.CharField(blank=True, help_text='The test payout txid', max_length=255),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='test_payout_tx_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]