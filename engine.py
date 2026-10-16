"""Expert Rubric Reliability. See METHODS.md for assumptions."""
def analyze(data):
    labels=data['labels']; rows=data['rows']
    if len(labels)<2 or len(set(labels))!=len(labels) or not rows:
        raise ValueError('Need distinct ordered labels and nonempty ratings')
    index={v:i for i,v in enumerate(labels)}; k=len(labels); n=len(rows)
    matrix=[[0]*k for _ in labels]
    for r in rows:
        if r['a'] not in index or r['b'] not in index: raise ValueError('Unknown rating')
        matrix[index[r['a']]][index[r['b']]]+=1
    a=[sum(row) for row in matrix]; b=[sum(row[j] for row in matrix) for j in range(k)]
    observed=sum(matrix[i][i] for i in range(k))/n
    expected=sum(a[i]*b[i] for i in range(k))/n**2
    wd=sum((i-j)**2*matrix[i][j]/n for i in range(k) for j in range(k))
    we=sum((i-j)**2*a[i]*b[j]/n**2 for i in range(k) for j in range(k))
    return {'n':n,'labels':labels,'confusion_matrix':matrix,'agreement':observed,
            'cohen_kappa':(observed-expected)/(1-expected) if expected<1 else None,
            'quadratic_weighted_kappa':1-wd/we if we else None,
            'adjudication':[r for r in rows if r['a']!=r['b']]}
