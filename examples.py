# Example usage:
if __name__ == '__main__':
    from weighting.constants import DB_TOLERANCE
    from weighting.constants import ITU_R_468_FREQS_AND_EXPECTED_VALUES
    from weighting.filter import r468

    print('\nSimple usage examples:\n')
    print('r468(1000):', r468(1000))
    print('r468(1000, \'1kHz\'):', r468(1000, '1kHz'))
    print('r468(1000, \'2kHz\'):', r468(1000, '2kHz'))

    print('\nWith 1 kHz option:\n')
    for f in ITU_R_468_FREQS_AND_EXPECTED_VALUES:
        print(f[0], r468(f[0], '1kHz'))

    print('\nWith 2 kHz option:\n')
    for f in ITU_R_468_FREQS_AND_EXPECTED_VALUES:
        print(f[0], r468(f[0], '2kHz'))

    print('\nFind max dB difference:\n')
    db_values = []
    for f in ITU_R_468_FREQS_AND_EXPECTED_VALUES:
        db_values.append(abs(f[1] - r468(f[0])))
    print(max(db_values))
    print('Expected:', DB_TOLERANCE)
    print('Value <= Expected?:', abs(f[1] - r468(f[0])) <= DB_TOLERANCE)

    # Run all possible integer values
    for i in range(1, 96001):
        r468(i, '1kHz')
