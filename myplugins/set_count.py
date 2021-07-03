from itertools import chain

from pelican import signals


def tag_count(generator):
    tag_count = {}
    for tag, articles in generator.tags.items():
        count = len(articles)
        tag_count[tag.name] = count
        setattr(tag, "count", count)

    category_count = {}
    for category, articles in generator.categories:
        count = len(articles)
        category_count[category.name] = count
        setattr(category, "count", count)

    for article in chain(generator.articles, generator.drafts):
        for tag in article.tags:
            setattr(tag, "count", tag_count.get(tag.name, 0))
        setattr(article.category, "count",
                category_count.get(article.category.name, 0))


def register():
    signals.article_generator_finalized.connect(tag_count)
