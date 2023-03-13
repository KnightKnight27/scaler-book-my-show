from ..models import ShowSeat
from ..models import ShowSeatStatus
from ..models import Ticket
from ..models import TicketStatus
from TicketCalculatorServices import TicketCalculatorService
from django.db import transaction
from ..models import User


class BookTicketService:

    @transaction.atomic
    def book_ticket(self, user_id, show_seat_ids):
        show_seats = ShowSeat.get_all_seats_by_id(show_seat_ids)
        user = User.objects.filter(id=user_id)
        for show_seat in show_seats:
            if show_seat.show_seat_status != ShowSeatStatus.AVAILABLE:
                raise Exception("SEAT IS NOT AVAILABLE")
        show = show_seats[0].how_seat_show
        for show_seat in show_seats:

            show_seat.show_seat_status = ShowSeatStatus.LOCKED
            # THIS IS NOT A DATABASE LOCK
            # YOU CAN ARE EXCLUSIVELY PUTTING A STATUS LOCK
            show_seat.save()

        ticket = Ticket()
        ticket.ticket_status = TicketStatus.PAYMENT_PENDING
        ticket.ticket_show = show
        ticket.show_seats = show_seats
        ticket.total_amount = TicketCalculatorService().TicketCalculatorService
        ticket.booked_by = user
        ticket.save()

        return ticket