# Generated by Django 5.1.4 on 2025-01-09 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectorTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, help_text='数据是否假删除')),
                ('connector_task_id', models.UUIDField(db_index=True, unique=True)),
                ('task_id', models.CharField(db_index=True, help_text='关联任务id', max_length=50)),
                ('org_id', models.CharField(help_text='组织id', max_length=50)),
                ('uscc', models.CharField(default='', help_text='组织社会信用代码', max_length=20)),
                ('contract_id', models.CharField(help_text='合约id', max_length=50)),
                ('activity_code', models.CharField(help_text='活动编号', max_length=50)),
                ('connector_code', models.CharField(help_text='连接器编码', max_length=50)),
                ('event_action_id', models.CharField(default='', help_text='触发事件id/执行动作id', max_length=50)),
                ('event_action_params', models.JSONField(default=dict, help_text='触发事件/执行动作 的执行参数(json格式字符串)')),
                ('status', models.CharField(choices=[('default', ''), ('waiting', '等待中'), ('running', '运行中'), ('stopped', '已停止'), ('failed', '失败'), ('warning', '异常'), ('done', '完成')], default='default', help_text='任务状态', max_length=30)),
                ('status_update_at', models.DateTimeField(null=True, verbose_name='最新状态变更时间')),
                ('is_send_qty', models.BooleanField(default=False, help_text='是否上报协作数')),
                ('target_qty', models.IntegerField(default=0, help_text='目标总量')),
                ('done_qty', models.IntegerField(default=0, help_text='已完成数量')),
                ('transfer_id', models.CharField(default='', help_text='传输身份id', max_length=50)),
                ('transfer_receive_config', models.JSONField(default=dict, help_text='传输接收队列配置')),
                ('transfer_send_config', models.JSONField(default=dict, help_text='传输发送队列配置')),
                ('task_from', models.CharField(help_text='任务来源(连接器)', max_length=50)),
                ('err_msg', models.TextField(default='', help_text='错误信息')),
            ],
            options={
                'db_table': 'connector_task',
            },
        ),
        migrations.CreateModel(
            name='ConnectorTaskLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, help_text='数据是否假删除')),
                ('log_id', models.UUIDField(db_index=True, unique=True)),
                ('connector_task_id', models.UUIDField(db_index=True, help_text='关联任务id')),
                ('err_msg', models.TextField(default='', help_text='错误信息')),
                ('process', models.CharField(choices=[('waiting', '等待中'), ('params_check', '参数检查'), ('execute', '任务执行'), ('response_handler', '响应处理'), ('up_chain', '上链'), ('publish', '发送消息'), ('done', '完成')], default='waiting', help_text='任务处理进度', max_length=20)),
                ('success', models.BooleanField(default=True, help_text='是否成功')),
            ],
            options={
                'db_table': 'connector_task_log',
            },
        ),
        migrations.CreateModel(
            name='QueueMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, help_text='数据是否假删除')),
                ('message_id', models.UUIDField(db_index=True, unique=True)),
                ('connector_task_id', models.UUIDField(db_index=True, help_text='关联任务id', null=True)),
                ('message', models.BinaryField(help_text='原始报文')),
                ('queue_info', models.JSONField(default=dict, help_text='队列信息')),
                ('status', models.CharField(choices=[('waiting', '等待中'), ('running', '运行中'), ('failed', '执行失败'), ('success', '执行成功')], default='waiting', help_text='状态', max_length=30)),
            ],
            options={
                'db_table': 'connector_queue_message',
            },
        ),
    ]
