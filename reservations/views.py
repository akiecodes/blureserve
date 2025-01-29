from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Seat, Reservation
from .serializers import SeatSerializer, ReservationSerializer
from django.http import HttpResponse

class ReserveSeat(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        available_seats = Seat.objects.filter(is_reserved=False)
        if available_seats.exists():
            seat = available_seats.first()
            seat.is_reserved = True
            seat.save()
            reservation = Reservation.objects.create(employee=request.user, seat=seat)
            return Response(ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED)
        return Response({"error": "No seats available"}, status=status.HTTP_400_BAD_REQUEST)

class CancelReservation(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            reservation = Reservation.objects.get(employee=request.user)
            reservation.seat.is_reserved = False
            reservation.seat.save()
            reservation.delete()
            return Response({"message": "Reservation cancelled"}, status=status.HTTP_200_OK)
        except Reservation.DoesNotExist:
            return Response({"error": "No active reservation found"}, status=status.HTTP_404_NOT_FOUND)

class ListReservations(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


def index(request):
    return HttpResponse("Reservations App is working!")

