def findMostPopularTopic(postDetails):
    
    from collections import defaultdict

    topic_scores = defaultdict(int)

    for post in postDetails:
        parts = post.split(",")
        if len(parts) != 5:
            return "Invalid Input" 

        try:
            _, topic, likes, comments, shares = parts
            likes, comments, shares = int(likes), int(comments), int(shares)

            post_score = likes * 5 + comments * 3 + shares * 2

            topic_scores[topic] += post_score
        except ValueError:
            return "Invalid Input"

    most_popular_topic = max(topic_scores, key=topic_scores.get)
    return most_popular_topic

post_details = [
    "A101,Topic A,1000,2500,500",
    "B001,Topic A,450,145,5",
    "A201,Topic A,200,650,100",
    "C501,Topic A,25000,12750,2000"
]

print(findMostPopularTopic(post_details))
