def partition(arr, classifier_method):
    return [x for x in arr if classifier_method(x)], [x for x in arr if not classifier_method(x)]