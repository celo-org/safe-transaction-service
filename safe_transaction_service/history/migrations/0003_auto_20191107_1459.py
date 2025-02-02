# Generated by Django 2.2.7 on 2019-11-07 14:59

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import model_utils.fields

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20190725_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='EthereumBlock',
            fields=[
                ('number', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('gas_used', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField()),
                ('block_hash', gnosis.eth.django.models.Sha3HashField(unique=True)),
                ('parent_hash', gnosis.eth.django.models.Sha3HashField(unique=True)),
                ('confirmed', models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EthereumTx',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('tx_hash', gnosis.eth.django.models.Sha3HashField(primary_key=True, serialize=False, unique=True)),
                ('gas_used', gnosis.eth.django.models.Uint256Field(default=None, null=True)),
                ('status', models.IntegerField(default=None, null=True)),
                ('transaction_index', models.PositiveIntegerField(default=None, null=True)),
                ('_from', gnosis.eth.django.models.EthereumAddressField(db_index=True, null=True)),
                ('gas', gnosis.eth.django.models.Uint256Field()),
                ('gas_price', gnosis.eth.django.models.Uint256Field()),
                ('data', models.BinaryField(null=True)),
                ('nonce', gnosis.eth.django.models.Uint256Field()),
                ('to', gnosis.eth.django.models.EthereumAddressField(db_index=True, null=True)),
                ('value', gnosis.eth.django.models.Uint256Field()),
                ('block', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='txs', to='history.EthereumBlock')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InternalTx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', gnosis.eth.django.models.EthereumAddressField(db_index=True, null=True)),
                ('gas', gnosis.eth.django.models.Uint256Field()),
                ('data', models.BinaryField(null=True)),
                ('to', gnosis.eth.django.models.EthereumAddressField(db_index=True, null=True)),
                ('value', gnosis.eth.django.models.Uint256Field()),
                ('gas_used', gnosis.eth.django.models.Uint256Field()),
                ('contract_address', gnosis.eth.django.models.EthereumAddressField(db_index=True, null=True)),
                ('code', models.BinaryField(null=True)),
                ('output', models.BinaryField(null=True)),
                ('refund_address', gnosis.eth.django.models.EthereumAddressField(db_index=True, null=True)),
                ('tx_type', models.PositiveSmallIntegerField(choices=[(0, 'CALL'), (1, 'CREATE'), (2, 'SELF_DESTRUCT')], db_index=True)),
                ('call_type', models.PositiveSmallIntegerField(choices=[(0, 'CALL'), (1, 'DELEGATE_CALL')], db_index=True, null=True)),
                ('trace_address', models.CharField(max_length=100)),
                ('error', models.CharField(max_length=100, null=True)),
                ('ethereum_tx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internal_txs', to='history.EthereumTx')),
            ],
            options={
                'unique_together': {('ethereum_tx', 'trace_address')},
            },
        ),
        migrations.CreateModel(
            name='ProxyFactory',
            fields=[
                ('address', gnosis.eth.django.models.EthereumAddressField(primary_key=True, serialize=False)),
                ('initial_block_number', models.IntegerField(default=0)),
                ('tx_block_number', models.IntegerField(default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'Proxy factories',
                'ordering': ['tx_block_number'],
            },
        ),
        migrations.CreateModel(
            name='SafeMasterCopy',
            fields=[
                ('address', gnosis.eth.django.models.EthereumAddressField(primary_key=True, serialize=False)),
                ('initial_block_number', models.IntegerField(default=0)),
                ('tx_block_number', models.IntegerField(default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'Safe master copies',
                'ordering': ['tx_block_number'],
            },
        ),
        migrations.RemoveField(
            model_name='multisigtransaction',
            name='execution_date',
        ),
        migrations.RemoveField(
            model_name='multisigtransaction',
            name='mined',
        ),
        migrations.AddField(
            model_name='multisigconfirmation',
            name='multisig_transaction_hash',
            field=gnosis.eth.django.models.Sha3HashField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='multisigtransaction',
            name='signatures',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='multisigconfirmation',
            name='multisig_transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmations', to='history.MultisigTransaction'),
        ),
        migrations.AlterField(
            model_name='multisigconfirmation',
            name='signature',
            field=gnosis.eth.django.models.HexField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='multisigtransaction',
            name='to',
            field=gnosis.eth.django.models.EthereumAddressField(db_index=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='multisigconfirmation',
            unique_together={('multisig_transaction_hash', 'owner')},
        ),
        migrations.CreateModel(
            name='InternalTxDecoded',
            fields=[
                ('internal_tx', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='decoded_tx', serialize=False, to='history.InternalTx')),
                ('function_name', models.CharField(max_length=256)),
                ('arguments', django.contrib.postgres.fields.jsonb.JSONField()),
                ('processed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Internal txs decoded',
            },
        ),
        migrations.CreateModel(
            name='SafeContract',
            fields=[
                ('address', gnosis.eth.django.models.EthereumAddressField(primary_key=True, serialize=False)),
                ('erc20_block_number', models.IntegerField(default=0)),
                ('ethereum_tx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='safe_contracts', to='history.EthereumTx')),
            ],
        ),
        migrations.RemoveField(
            model_name='multisigconfirmation',
            name='block_date_time',
        ),
        migrations.RemoveField(
            model_name='multisigconfirmation',
            name='block_number',
        ),
        migrations.RemoveField(
            model_name='multisigconfirmation',
            name='confirmation_type',
        ),
        migrations.RemoveField(
            model_name='multisigconfirmation',
            name='mined',
        ),
        migrations.RemoveField(
            model_name='multisigconfirmation',
            name='transaction_hash',
        ),
        migrations.AddField(
            model_name='multisigconfirmation',
            name='ethereum_tx',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='multisig_confirmations', to='history.EthereumTx'),
        ),
        migrations.AddField(
            model_name='multisigtransaction',
            name='ethereum_tx',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='multisig_txs', to='history.EthereumTx'),
        ),
        migrations.CreateModel(
            name='SafeStatus',
            fields=[
                ('internal_tx', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='safe_status', serialize=False, to='history.InternalTx')),
                ('address', gnosis.eth.django.models.EthereumAddressField()),
                ('owners', django.contrib.postgres.fields.ArrayField(base_field=gnosis.eth.django.models.EthereumAddressField(), size=None)),
                ('threshold', gnosis.eth.django.models.Uint256Field()),
                ('nonce', gnosis.eth.django.models.Uint256Field(default=0)),
                ('master_copy', gnosis.eth.django.models.EthereumAddressField()),
            ],
            options={
                'verbose_name_plural': 'Safe statuses',
                'unique_together': {('internal_tx', 'address')},
            },
        ),
        migrations.CreateModel(
            name='EthereumEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_index', models.PositiveIntegerField()),
                ('address', gnosis.eth.django.models.EthereumAddressField(db_index=True)),
                ('topic', gnosis.eth.django.models.Sha3HashField(db_index=True)),
                ('topics', django.contrib.postgres.fields.ArrayField(base_field=gnosis.eth.django.models.Sha3HashField(), size=None)),
                ('arguments', django.contrib.postgres.fields.jsonb.JSONField()),
                ('ethereum_tx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='history.EthereumTx')),
            ],
            options={
                'unique_together': {('ethereum_tx', 'log_index')},
            },
        ),
    ]
