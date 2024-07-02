def convert_quads_to_tris(obj_filename, output_filename):
    with open(obj_filename, 'r') as f:
        lines = f.readlines()

    tri_lines = []
    for line in lines:
        if line.startswith('f'):
            vertices = line.strip().split()[1:]
            if len(vertices) == 4:  # Quadrilateral
                tri_lines.append(f'f {vertices[0]} {vertices[1]} {vertices[2]}\n')
                tri_lines.append(f'f {vertices[2]} {vertices[3]} {vertices[0]}\n')
            elif len(vertices) == 3:  # Triangle
                tri_lines.append(line)
        else:
            tri_lines.append(line)

    with open(output_filename, 'w') as f:
        f.writelines(tri_lines)

# Example usage
convert_quads_to_tris('AkulaClassAtackSubmarine.obj', 'AkulaClassAtackSubmarine_output.obj')
