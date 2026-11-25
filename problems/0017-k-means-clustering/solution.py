def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids=[tuple(c)for c in initial_centroids]
    
    dimensions=len(points[0])
    for iteration in range (max_iterations):
        clusters=[[] for _ in range (k)]
        for point in points:
            distances=[]
            for centroid in centroids:
                distance=sum((point[d]-centroid[d])**2 for d in range(dimensions))
                distances.append(distance) 
            nearest_cluster=distances.index(min(distances))
            clusters[nearest_cluster].append(point)
        new_centroids=[]
        for i in range (k):
            if len(clusters[i])==0:
                new_centroids.append(centroids[i])
                continue
            centroid=tuple(sum(point[d]for point in clusters[i])/len(clusters[i])for d in range (dimensions))
            new_centroids.append(centroid)
        converged=all(abs(new_centroids[i][d]-centroids[i][d])<1e-12 for i in range (k) for d in range(dimensions))
        centroids=new_centroids
        if converged:
            break

    final_centroids=list(tuple(round(value,4)for value in centroid)for centroid in centroids )



    return final_centroids