from ACDC import ACDC
from RELAX import RELAX
from PIL import Image, ImageDraw
import math

if __name__ == "__main__":
    acdc = ACDC("log4j-2.4_acdc_clustered.rsf")
    relax = RELAX("log4j-2.4_relax_clusters.rsf")

    clusters_pos = []
    categories_vectors = {}
    interval = math.pi * 2 / (len(relax.categories) - 1)
    cur_radian = -math.pi
    for category in relax.categories:
        categories_vectors[category] = (math.sin(cur_radian), math.cos(cur_radian))
        cur_radian += interval

    total = 0
    available = 0
    n_cluster = 0
    for cluster_name in acdc.clusters:
        n_cluster += 1
        pos_x = 0
        pos_y = 0

        cluster = acdc.clusters[cluster_name]
        for package in cluster:
            total += 1
            category = relax.packages.get(package, None)
            if not category:
                continue
            available += 1
            vector = categories_vectors[category]
            pos_y += vector[0]
            pos_x += vector[1]

        clusters_pos.append((pos_x, pos_y, len(cluster)))

    print(str(available) + "/" + str(total))
    print(n_cluster)

    im = Image.new("RGB", (2000, 2000), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for (x, y, s) in clusters_pos:
        draw.ellipse((x * 20 + 1000 - s / 2, y * 20 + 1000 - s / 2, x * 20 + 1000 + s / 2, y * 20 + 1000 + s / 2), fill='black')
    im.show()
