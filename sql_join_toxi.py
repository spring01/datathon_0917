
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
    sig_diseases.append('Other')
    print sig_diseases



    cur.execute("select interaction_actions, disease_id, inference_score " + \
                "from toxicogenomics_chemicals_binary tc " + \
                "join toxicogenomics_diseases td on tc.gene_id = td.gene_id and tc.chemical_name = td.inference_chemical_name ")
    result = cur.fetchall()
    print len(result)
    all_inter = []
    all_target = []
    all_score = []
    for i, res in enumerate(result):
        if i % 1000 == 0:
            print i
        interaction_actions, disease_id, inference_score = res
        all_inter.append(interaction_actions)
        target = np.zeros(len(sig_diseases) + 1, dtype=np.int32)
        if disease_id in sig_diseases:
            pos = sig_diseases.index(disease_id)
            target[pos] = 1
        else:
            target[-1] = 1
        all_target.append(target)
        all_score.append(inference_score)

all_inter = np.array(all_inter)
all_target = np.array(all_target)
all_score = np.array(all_score)
with open('inter_dis_score.p', 'wb') as pic:
    pickle.dump((all_inter, all_target, all_score, sig_diseases), pic)







