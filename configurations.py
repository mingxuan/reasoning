def get_config():
    config = {}
    config['nhids'] = 50
    config['nemb'] = 50
    config['n_layer'] = 3
    config['vocab_size'] = 24
    config['label_size'] = 12

    #####################
    datadir = './data/'

    ### raw training data and test data
    raw_train_file = datadir + 'qa19_path-finding_train.txt'
    raw_test_file = datadir + 'qa19_path-finding_test.txt'
    config['raw_train'] = raw_train_file
    config['raw_test'] = raw_test_file

    ###### temp data
    tmp_suffix = ['.fact', 'ques', '.answer']
    head_suffix = datadir+"pathfinding_19"
    config['train_file'] = [head_suffix+suffix for suffix in tmp_suffix]
    config['test_file'] = [head_suffix+suffix for suffix in tmp_suffix]

    ###### dict file
    config['dict_file'] = head_suffix + "dict.pkl"


    return config

