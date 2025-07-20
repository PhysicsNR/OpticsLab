import json

def save_system(elements, filename):
    serializable = []
    for elem in elements:
        data = elem.__dict__.copy()
        data['type'] = elem.__class__.__name__
        serializable.append(data)
    with open(filename, 'w') as f:
        json.dump(serializable, f, indent=2)

def load_system(filename):
    from core.optical_elements import FreeSpace, Lens, Mirror, CurvedMirror, Prism, Grating, Fiber
    with open(filename, 'r') as f:
        serializable = json.load(f)
    element_map = {
        'FreeSpace': FreeSpace,
        'Lens': Lens,
        'Mirror': Mirror,
        'CurvedMirror': CurvedMirror,
        'Prism': Prism,
        'Grating': Grating,
        'Fiber': Fiber
    }
    elements = []
    for data in serializable:
        cls = element_map[data.pop('type')]
        elements.append(cls(**data))
    return elements
