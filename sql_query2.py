
import psycopg2
from information import CONNECT
import numpy as np
import cPickle as pickle


if __name__ == '__main__':
    db_conn = psycopg2.connect(CONNECT)
    table_list = ['genes', 'gtex_donor', 'gtex_gene_expression_processed', 'gtex_gene_model',
        'gtex_sample', 'gtex_sample_expression', 'gtex_tissue', 'tcga', 'toxicogenomics_chemicals_binary', 'toxicogenomics_diseases']

    cur = db_conn.cursor()
    cur.execute("select disease_id, count(disease_id) co " + \
                "from toxicogenomics_diseases " + \
                "group by disease_id " + \
                "order by co desc")
    result = cur.fetchall()
    print len(result)
    print result[:15]
    sig_diseases = [res[0] for res in result[:15]]
    print sig_diseases

