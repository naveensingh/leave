from django.shortcuts import render


class PersonalProfileView(AbstractArticleView):
    template_name = 'personal_profile.html'

    def get(self, request):
        self.setup()
        article_model = ArticleContent
        posts = ArticleHelper.get_articles_filtered_by_team(article_model, self.team)
        paginated_results_for_searched_query = paginate_search_results(self.request, posts)

        context = {
            "articles": paginated_results_for_searched_query,
            "regions": self.regions,
            "permission": self.permission,
            'tags_list': self.tags_list,
            'content_type_list': self.content_type_list ,
            'commodities_list': self.commodities_list,
            "categories": self.categories,
            "years": self.years,
            "title": "Latest Articles",
            "page_id": "view_all_published_articles"
        }
        return render(request, self.template_name, context)