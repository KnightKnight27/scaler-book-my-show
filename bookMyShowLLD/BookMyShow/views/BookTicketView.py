from django.views import View

# WHEN USER HITS AN API
# TO book a ticker
#API
# /bookTicket
# THIS IS ACTING LIKE A CONTROLLER

class BookTicketView(View):

    def post(self, request):
        show_seat_ids = request.POST.get("show_seat_id")
        user_id = request.POST.get("user_id")
        try:
            ticket = request.book_ticket_service.book_ticket(user_id, show_seat_ids)
            serialized_ticket = {}
            response = {
                "ticket" : serialized_ticket
            }
            return response
        except:
            # IT IS PRETTY MUCH AN HTTP RESPONSE OBJECT
            response = { "status": "FAILED" }
            return response


        # 1. -> SEARCH FOR THESE SHOW SEATS.OR FETCH FROM DATABASE
        # 2. -> CHECK THEIR STATUS IF THEY ARE AVAILABLE
        # 3. -> IF THEY ARE NOT AVAILABLE
              # SOMETHING SOMETHING
        # 4. -> IF IT IS AVAILABLE
        # 5. -> (I will book these seats, but let's handle issues with concurrency)
        # 6. -> Payment
        # 7. -> Ticket will be issued
        # 8 -> return the response to user of failure or success
