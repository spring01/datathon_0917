
import psycopg2
from information import CONNECT



if __name__ == '__main__':
    db_conn = psycopg2.connect(CONNECT)
    table_list = ['genes', 'gtex_donor', 'gtex_gene_expression_processed', 'gtex_gene_model',
        'gtex_sample', 'gtex_sample_expression', 'gtex_tissue', 'tcga', 'toxicogenomics_chemicals', 'toxicogenomics_diseases']

    cur = db_conn.cursor()
    cur.execute("select * from toxicogenomics_chemicals")
    result = cur.fetchall()
    for r in result[:10]:
        print r
