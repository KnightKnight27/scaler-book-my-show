from ..services import BookTicketService


class BookTicketMiddleWare:
    def __int__(self, get_response):
        self.get_response = get_response
        self.book_ticket_service = BookTicketService.BookTicketService()

    def __call__(self, request):
        request.book_ticket_service = self.book_ticket_service
        response = self.get_reponse(request)
        return response