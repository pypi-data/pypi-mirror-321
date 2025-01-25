
import numpy as np
def topsis(data,weights,impacts):
  # Normalising the data
  normalised=data/np.sqrt(np.sum(data**2,axis=0))
  weighted=normalised*weights
  # Best ideal and worst ideal solns
  best_ideal=np.where(np.array(impacts)=='+',np.max(weighted,axis=0),np.min(weighted,axis=0))
  worst_ideal=np.where(np.array(impacts)=='+',np.min(weighted,axis=0),np.max(weighted,axis=0))
  # Eucledian distance
  dist_best=np.sqrt(np.sum((weighted-best_ideal)**2,axis=1))
  dist_worst=np.sqrt(np.sum((weighted-worst_ideal)**2,axis=1))
  # Performance Scores
  performance_scores=dist_worst/(dist_best+dist_worst)
  # Ranking
  rankings=np.argsort(performance_scores)[::-1] + 1
  return rankings.tolist(), performance scores.tolist()
  