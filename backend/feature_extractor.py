import pefile

def get_resource_size(resource_dir):
    size = 0
    if hasattr(resource_dir, 'entries'):
        for entry in resource_dir.entries:
            if hasattr(entry, 'directory'):
                size += get_resource_size(entry.directory)
            elif hasattr(entry, 'data'):
                size += entry.data.struct.Size
    return size

def extract_features(filepath):
    try:
        pe = pefile.PE(filepath)
    except:
        # If invalid PE file, return zeros for all features
        return {k: 0 for k in [
            'Machine','DebugSize','DebugRVA','MajorImageVersion','MajorOSVersion',
            'ExportRVA','ExportSize','IatVRA','MajorLinkerVersion','MinorLinkerVersion',
            'NumberOfSections','SizeOfStackReserve','DllCharacteristics','ResourceSize','BitcoinAddresses'
        ]}

    fh = pe.FILE_HEADER
    oh = pe.OPTIONAL_HEADER

    features = {
        'Machine': getattr(fh, 'Machine', 0),
        'DebugSize': getattr(oh, 'DebugSize', 0),
        'DebugRVA': getattr(oh, 'DebugRVA', 0),
        'MajorImageVersion': getattr(oh, 'MajorImageVersion', 0),
        'MajorOSVersion': getattr(oh, 'MajorOperatingSystemVersion', 0),
        'ExportRVA': getattr(oh, 'ExportRVA', 0),
        'ExportSize': getattr(oh, 'SizeOfCode', 0),
        'IatVRA': getattr(oh, 'IatRVA', 0),
        'MajorLinkerVersion': getattr(fh, 'MajorLinkerVersion', 0),
        'MinorLinkerVersion': getattr(fh, 'MinorLinkerVersion', 0),
        'NumberOfSections': getattr(fh, 'NumberOfSections', 0),
        'SizeOfStackReserve': getattr(oh, 'SizeOfStackReserve', 0),
        'DllCharacteristics': getattr(oh, 'DllCharacteristics', 0),
        'ResourceSize': get_resource_size(getattr(pe, 'DIRECTORY_ENTRY_RESOURCE', [])),
        'BitcoinAddresses': 0  # placeholder
    }

    return features

