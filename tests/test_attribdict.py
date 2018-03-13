import datetime
import json
import multiprocessing
import pickle

from attribdict import AttribDict


def test_attribdict_attributes():
    adict = AttribDict()
    adict.is_complete = True
    adict.starting_date = datetime.datetime(2017, 1, 1, 0, 0)

    assert adict
    assert adict.starting_date == datetime.datetime(2017, 1, 1, 0, 0)
    assert adict['starting_date'] == datetime.datetime(2017, 1, 1, 0, 0)

    assert adict == {'is_complete': True, 'starting_date': datetime.datetime(2017, 1, 1, 0, 0)}


def test_dict_is_pickable(tmpdir):
    adict = AttribDict({'starting_date': datetime.datetime(2017, 1, 1, 0, 0)})
    assert adict

    temporary_file_name = '{}/test_pickle_file_{}.p'.format(tmpdir, datetime.datetime.now().isoformat())

    pickle_file = open(temporary_file_name, 'wb')
    pickle.dump(adict, pickle_file)
    pickle_file.close()

    assert pickle.load(open(temporary_file_name, 'rb')) == adict


def random_test_function(item):
    item.additional = 'additional value'
    return item


def test_dict_supports_multiprocessing():
    adict = AttribDict({'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'})

    list_of_adicts = [adict] * 30

    with multiprocessing.Pool() as pool:
        results = pool.map(random_test_function, list_of_adicts)

    assert len(results) == 30

    for item in results:
        assert item['additional'] == 'additional value'

def test_is_serializable():
    adict = AttribDict({'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'})
    json.dumps(adict)
