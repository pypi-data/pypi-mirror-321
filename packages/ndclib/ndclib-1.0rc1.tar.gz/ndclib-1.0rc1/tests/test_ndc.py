from contextlib import nullcontext

import pytest

from ndclib import NDC, RxNormAPIProvider
from ndclib.exceptions import UndefinedOutputException
from ndclib.ndc import HyphenatedNDC10
from ndclib.format import NDCFormat


def test__retry_data_provider():
    n = NDC("1234-5678-90")
    assert n._data_provider is None

    n._retry_data_provider()
    assert type(n._data_provider) is RxNormAPIProvider


def test_set_provider():
    n = NDC("1234-5678-90")
    data_provider = RxNormAPIProvider()

    # Use set_provider on the expected class to be instantiated based on the
    # input NDC. This ensures that our assertion is comparing to the exact
    # object expected. The different NDC classes each get their own reference to
    # the data provider class.
    HyphenatedNDC10.set_provider(data_provider)
    assert n._data_provider is data_provider


@pytest.mark.parametrize(
    "generic_ndc,ndc_format",
    [
        ("0378-4517-93", NDCFormat._4_4_2),
        ("00378451793", NDCFormat._4_4_2),
        ("0378451793", NDCFormat._4_4_2),
        ("00378-4517-93", NDCFormat._4_4_2),
        ("70377-027-11", NDCFormat._5_3_2),
        ("70377002711", NDCFormat._5_3_2),
        ("7037702711", NDCFormat._5_3_2),
        ("70377-0027-11", NDCFormat._5_3_2),
        ("60505-3484-3", NDCFormat._5_4_1),
        ("60505348403", NDCFormat._5_4_1),
        ("6050534843", NDCFormat._5_4_1),
        ("60505-3484-03", NDCFormat._5_4_1),
        ("12345-67890", NDCFormat._5_5),
        ("1234-567890", NDCFormat._4_6),
    ],
)
def test__calculate_format(generic_ndc, ndc_format):
    NDC.set_provider(RxNormAPIProvider())
    n = NDC(generic_ndc)
    assert n._calculate_format() == ndc_format


@pytest.mark.parametrize(
    "generic_ndc,ndc10",
    [
        ("0378-4517-93", "0378-4517-93"),
        ("00378451793", "0378-4517-93"),
        ("0378451793", "0378-4517-93"),
        ("00378-4517-93", "0378-4517-93"),
        ("70377-027-11", "70377-027-11"),
        ("70377002711", "70377-027-11"),
        ("7037702711", "70377-027-11"),
        ("70377-0027-11", "70377-027-11"),
        ("60505-3484-3", "60505-3484-3"),
        ("60505348403", "60505-3484-3"),
        ("6050534843", "60505-3484-3"),
        ("60505-3484-03", "60505-3484-3"),
        ("12345-67890", "12345-67890"),
        ("1234-567890", "1234-567890"),
    ],
)
def test_as_ndc10_hyphenated(generic_ndc, ndc10):
    n = NDC(generic_ndc)
    assert n.to_10(hyphenated=True) == ndc10


@pytest.mark.parametrize(
    "generic_ndc,ndc10",
    [
        ("0378-4517-93", "0378451793"),
        ("00378451793", "0378451793"),
        ("0378451793", "0378451793"),
        ("00378-4517-93", "0378451793"),
        ("70377-027-11", "7037702711"),
        ("70377002711", "7037702711"),
        ("7037702711", "7037702711"),
        ("70377-0027-11", "7037702711"),
        ("60505-3484-3", "6050534843"),
        ("60505348403", "6050534843"),
        ("6050534843", "6050534843"),
        ("60505-3484-03", "6050534843"),
        ("12345-67890", "1234567890"),
        ("1234-567890", "1234567890"),
    ],
)
def test_as_ndc10_unhyphenated(generic_ndc, ndc10):
    n = NDC(generic_ndc)
    assert n.to_10(hyphenated=False) == ndc10


@pytest.mark.parametrize(
    "generic_ndc,expectation",
    [
        ("0378-4517-93", nullcontext("00378-4517-93")),
        ("00378451793", nullcontext("00378-4517-93")),
        ("0378451793", nullcontext("00378-4517-93")),
        ("00378-4517-93", nullcontext("00378-4517-93")),
        ("70377-027-11", nullcontext("70377-0027-11")),
        ("70377002711", nullcontext("70377-0027-11")),
        ("7037702711", nullcontext("70377-0027-11")),
        ("70377-0027-11", nullcontext("70377-0027-11")),
        ("60505-3484-3", nullcontext("60505-3484-03")),
        ("60505348403", nullcontext("60505-3484-03")),
        ("6050534843", nullcontext("60505-3484-03")),
        ("60505-3484-03", nullcontext("60505-3484-03")),
        ("12345-67890", pytest.raises(UndefinedOutputException)),
        ("1234-567890", pytest.raises(UndefinedOutputException)),
    ],
)
def test_as_ndc11_hyphenated(generic_ndc, expectation):
    n = NDC(generic_ndc)
    with expectation as e:
        assert n.to_11(hyphenated=True) == e


@pytest.mark.parametrize(
    "generic_ndc,ndc11",
    [
        ("0378-4517-93", "00378451793"),
        ("00378451793", "00378451793"),
        ("0378451793", "00378451793"),
        ("00378-4517-93", "00378451793"),
        ("70377-027-11", "70377002711"),
        ("70377002711", "70377002711"),
        ("7037702711", "70377002711"),
        ("70377-0027-11", "70377002711"),
        ("60505-3484-3", "60505348403"),
        ("60505348403", "60505348403"),
        ("6050534843", "60505348403"),
        ("60505-3484-03", "60505348403"),
        ("12345-67890", "12345067890"),
        ("1234-567890", "01234567890"),
    ],
)
def test_as_ndc11_unhyphenated(generic_ndc, ndc11):
    n = NDC(generic_ndc)
    assert n.to_11(hyphenated=False) == ndc11
