from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credentials_id="",
                 sql="",
                 table="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id=redshift_conn_id
        self.aws_credentials_id=aws_credentials_id
        self.sql=sql
        self.table=table

    def execute(self, context):
        self.log.info('In load_fact: ')
        #aws_hook = AwsHook(self.aws_credentials_id)
        #credentials = aws_hook.get_credentials()
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        sql_statement = 'INSERT INTO %s %s' % (self.table, self.sql)
        redshift.run(sql_statement)
        self.log.info('load_fact is done')