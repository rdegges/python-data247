# python-data247

An API client for [Data 24-7](https://www.data24-7.com/).


## Install

To install the library, you can use
[pip](http://www.pip-installer.org/en/latest/).

```bash
$ pip install data247
```


## Usage

Essentially all you need to do is create a `Data247` client object--this holds
your account credentials and also specifies which data you're requesting.

You can then make queries using the `get` method, passing in the search term.

```python
>>> from data247 import Data247, IP
>>>
>>> client = Data247('myusername', 'mypassword', IP)
>>> client.get('174.134.29.20')
{
    u'city': u'Bakersfield',
    u'areacode': u'661',
    u'country': u'US',
    u'dst': u'1',
    u'zipcode': u'93312',
    u'longitude': u'-119.227203',
    u'state': u'CA',
    u'cost': u'0.0030',
    u'billable': u'1',
    u'latitude': u'35.383202',
    u'timezone': u'-8',
    u'ip_address': u'174.134.29.20'
}
```
