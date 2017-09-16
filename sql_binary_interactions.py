
import psycopg2
from information import CONNECT



if __name__ == '__main__':
    db_conn = psycopg2.connect(CONNECT)
    table_list = ['genes', 'gtex_donor', 'gtex_gene_expression_processed', 'gtex_gene_model',
        'gtex_sample', 'gtex_sample_expression', 'gtex_tissue', 'tcga', 'toxicogenomics_chemicals', 'toxicogenomics_diseases']

    cur = db_conn.cursor()
    cur.execute("select * from toxicogenomics_chemicals")
    table = cur.fetchall()
    all_keys = []
    for i in range(len(table)):
        tup = table[i]
        keys = tup[-1].split('|')
        for key in keys:
            if key not in all_keys:
                all_keys.append(key)

    print ', '.join(all_keys)
    print len(all_keys)
    print all_keys[7], all_keys[25], all_keys[36], all_keys[27],  all_keys[9]

    #~ new_header = 'gene_id,chemical_name,chemical_id,gene_forms,interactions,interaction_actions'
    #~ print new_header
    #~ for i in range(len(table)):
        #~ tup = table[i]
        #~ info = tup[-1]
        #~ vector = []
        #~ for key in all_keys:
            #~ if key in info:
                #~ vector.append('1')
            #~ else:
                #~ vector.append('0')
        #~ new_list = []
        #~ for ele in tup[:-1]:
            #~ if ele is None:
                #~ new_list.append('')
            #~ else:
                #~ new_list.append('"' + ele + '"')
        #~ vector_str = ',"{' + ','.join(vector) + '}"'
        #~ print ','.join(new_list) + vector_str
