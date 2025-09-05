def findMostPopularTopic(postDetails):
    from collections import defaultdict

    if not postDetails:
        return "Invalid input"

    topic_scores = defaultdict(int)
    topics = set()

    for post in postDetails:
        try:
            parts = post.strip().split(',')
            if len(parts) != 5:
                return "Invalid input"

            post_id, topic, likes, comments, shares = parts
            likes, comments, shares = int(likes.strip()), int(comments.strip()), int(shares.strip())

            if likes < 0 or comments < 0 or shares < 0:
                return "Invalid input"

            engagement_score = likes * 5 + comments * 3 + shares * 2
            topic_scores[topic] += engagement_score
            topics.add(topic)

        except (ValueError, IndexError):
            return "Invalid input"

    if len(topics) < 2:
        return "Invalid input"

    return max(topic_scores, key=topic_scores.get)

# Example usage
post_details = [
    "A101,Topic A,1000,2500,500",
    "B001,Topic A,450,145,5",
    "A201,Topic A,200,650,100",
    "C501,Topic A,25000,12750,2000"
]

print(findMostPopularTopic(post_details))
