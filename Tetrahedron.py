import multiprocessing
from multiprocessing import Pool

def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for index, line in enumerate(file):
            line = line.strip()
            if line:
                try:
                    x, y, z, n = map(float, line.strip('()\n').split(','))
                    points.append((x, y, z, int(n), index))
                except ValueError as e:
                    print(f"Error processing line: {line}")
                    print(e)
    return points

def volume_of_tetrahedron(combination):
    
    p1, p2, p3, p4 = combination
    AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
    AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

    cross_product_x = AB[1] * AC[2] - AB[2] * AC[1]
    cross_product_y = AB[2] * AC[0] - AB[0] * AC[2]
    cross_product_z = AB[0] * AC[1] - AB[1] * AC[0]

    scalar_triple_product = (
        AD[0] * cross_product_x +
        AD[1] * cross_product_y +
        AD[2] * cross_product_z
    )

    volume = abs(scalar_triple_product) / 6.0

    return volume, combination


def find_valid_tetrahedrons(points):
    points.sort(key=lambda p: p[3])  # Sort points based on the 'n' value
    n = len(points)
    valid_tetrahedrons = []
   

    for i in range(n):
        if i > 0 and points[i][3] == points[i-1][3]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and points[j][3] == points[j-1][3]:
                continue
            k, l = j + 1, n - 1
            while k < l:
                total = points[i][3] + points[j][3] + points[k][3] + points[l][3]
                if total == 100:
                    valid_tetrahedrons.append((points[i], points[j], points[k], points[l]))
                    # print("")
                    print(f" Found valid combination: {points[i][:4]}, {points[j][:4]}, {points[k][:4]}, {points[l][:4]} \n indexes for above valid combination : {points[i][4]}, {points[j][4]}, {points[k][4]}, {points[l][4]}\n")
                    while k < l and points[k][3] == points[k+1][3]:
                        k += 1
                    while k < l and points[l][3] == points[l-1][3]:
                        l -= 1
                    k += 1
                    l -= 1
                elif total < 100:
                    k += 1
                else:
                    l -= 1
    print(f"\n Total valid tetrahedrons found: {len(valid_tetrahedrons)}")
    return valid_tetrahedrons


def find_smallest_tetrahedron( valid_tetrahedrons, count=4):
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(volume_of_tetrahedron, [combination for combination in valid_tetrahedrons])
    
    results.sort(key=lambda x: x[0])
    return results[:count]
    

def main():
    points_large = read_points('points_small.txt')

    print(f"\n Number of points in file: {len(points_large)}\n")

    valid_tetrahedrons_large = find_valid_tetrahedrons(points_large)

    if not valid_tetrahedrons_large:
        print("\n No valid tetrahedrons found in file")
    else:
        print("\n Starting to find the smallest tetrahedron...")
        smallest_tetrahedron_large = find_smallest_tetrahedron(valid_tetrahedrons_large, count=4)
        for i, (volume, combination) in enumerate(smallest_tetrahedron_large):
            ind = [ind[4] for ind in combination]
            print(f"\nSmallest Tetrahedron {i+1} for file: {sorted(ind)} with volume: {volume}")


if __name__ == '__main__':
    main()
