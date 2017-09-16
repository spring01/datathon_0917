
import psycopg2
from information import CONNECT
import numpy as np
import cPickle as pickle


if __name__ == '__main__':
    db_conn = psycopg2.connect(CONNECT)
    table_list = ['genes', 'gtex_donor', 'gtex_gene_expression_processed', 'gtex_gene_model',
        'gtex_sample', 'gtex_sample_expression', 'gtex_tissue', 'tcga', 'toxicogenomics_chemicals_binary', 'toxicogenomics_diseases']

    cur = db_conn.cursor()
    cur.execute("select * " + \
                "from toxicogenomics_chemicals_binary ")
    result = cur.fetchall()
    all_forms = []
    for res in result:
        form = res[3]
        if form not in all_forms:
            all_forms.append(form)
    print len(all_forms), len(result)

    feat_mat = []
    target_mat = []
    for res in result:
        feature = res[-1]
        target = []
        for form in all_forms:
            if res[3] == form:
                target.append(1)
            else:
                target.append(0)
        feat_mat.append(feature)
        target_mat.append(target)

feat_mat = np.array(feat_mat)
target_mat = np.array(target_mat)
with open('chembin_form.p', 'wb') as pic:
    pickle.dump((feat_mat, target_mat, all_forms), pic)
