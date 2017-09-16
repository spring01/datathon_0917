
import psycopg2
from information import CONNECT, DATAPATH


def ts_sql_table_drop_create(db_conn, table_name, create_sql_cols, drop=True):
    cur = db_conn.cursor()
    if drop:
        try:
            cur.execute("DROP TABLE %s" % table_name)
        except psycopg2.Error:
            db_conn.commit()
    db_conn.commit()
    cur.execute("CREATE TABLE %s (%s)" % (table_name, create_sql_cols));
    db_conn.commit();
    cur.close();

def ts_sql_load_table_from_file(db_conn, table_name, col_fmt, file_name, delim):
    cur = db_conn.cursor()
    cur.execute("COPY %s(%s) FROM '%s' DELIMITER AS '%s' CSV HEADER" % (table_name, col_fmt, file_name, delim))
    db_conn.commit()
    cur.close()
    print "Loaded data from %s" % (file_name)

def load_csv(basename, header_type=None):
    fullname = basename + '.csv'
    fullpath = DATAPATH + fullname
    with open(fullpath) as csv:
        header = csv.next().strip()
    header_splitted = header.split(',')
    header_splitted_type = [h + ' text' for h in header_splitted]
    if header_type is not None:
        for i in range(len(header_splitted_type)):
            for tup in header_type:
                if tup[0] in header_splitted_type[i]:
                    header_splitted_type[i] = header_splitted[i] + ' ' + tup[1]
    header_type = ', '.join(header_splitted_type)
    ts_sql_table_drop_create(db_conn, basename, header_type)
    ts_sql_load_table_from_file(db_conn, basename, header, fullpath, ',')
    cur = db_conn.cursor()
    cur.execute("select * from " + basename)
    print header
    print cur.fetchone()


if __name__ == '__main__':
    db_conn = psycopg2.connect(CONNECT)
    basename_list = ['genes', 'gtex_gene_model',
        'gtex_sample', 'gtex_tissue', 'toxicogenomics_chemicals']
    for basename in basename_list:
        load_csv(basename)
    special_list = [('gtex_donor', [('age', 'integer')]),
                    ('gtex_gene_expression_processed', [('rpkm_expressions', 'float[]')]),
                    ('gtex_sample_expression', [('rpkm_expression', 'float')]),
                    ('tcga', [('fpkm_expression', 'float')]),
                    ('toxicogenomics_diseases', [('inference_score', 'float')]),
                    ('toxicogenomics_chemicals_binary', [('interaction_actions', 'int[]')])]
    for special in special_list:
        load_csv(*special)



