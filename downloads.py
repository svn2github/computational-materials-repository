downloads = [
    ('dssc', ['dssc.db']),
    ('dcdft', ['dcdft.db', 'dcdft_gpaw_pw_paw09.db']),
    ('beef', ['molecules.db', 'solids.db']),
    ('mp_gllbsc', ['mp_gllbsc.db']),
    ('organometal', ['organometal.db']),
    ('cubic_perovskites', ['cubic_perovskites.db']),
    ('low_symmetry_perovskites', ['low_symmetry_perovskites.db']),
    ('c2dm', ['c2dm.db']),
    ('vdwh', ['chi-data.tar.gz']),
    ('tmfp06d', ['tmfp06d.db']),
    ('absorption_perovskites', ['absorption_perovskites.db']),
    ('funct_perovskites', ['funct_perovskites.db']),
    ('fcc111', ['fcc111.db']),
    ('compression', ['compression.db']),
    ('gbrv', ['gbrv.db'])]

# Add pictures for the front-page:
downloads += [('.', [dir + '.png' for dir, names in downloads])]
