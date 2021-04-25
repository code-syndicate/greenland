from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import BankAccount, TransferRequest, OTP
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from .forms import LocalTransferForm, IntlTransferForm, SigninForm, VerifyOTPForm


def LogoutView(request):
    logout(request)
    context = {
        'msg': 'You have successfully logged out.',
        'color': 'green',
        'text_color': 'white',
    }
    return render(request, 'banking/index.html', context)


class IndexView(View):
    def get(self, request):
        # print(request.path)
        return render(request, 'banking/index.html')


class verifyView(LoginRequiredMixin, View):
    def get(self, request, reqID):
        context = {
            'reqID': reqID,
        }
        return render(request, 'banking/verifyotp.html', context)

    def post(self, request):
        form = VerifyOTPForm(request.POST)
        transfer = None
        if form.is_valid():
            try:
                transfer = TransferRequest.objects.get(
                    pk=form.cleaned_data['reqID'])
            except TransferRequest.DoesNotExist:
                context = {
                    'msg': 'Invalid Reference',
                    'color': 'red',
                    'reqID': form.cleaned_data['reqID'],
                }
                return render(request, 'banking/verifyotp.html', context)
            else:
                otp_object = OTP.check_otp_against_user(
                    form.cleaned_data['otp'], request.user)

            if not otp_object:
                context = {
                    'msg': 'Unauthorized Code',
                    'color': 'red',
                    'reqID': form.cleaned_data['reqID'],
                }
                return render(request, 'banking/verifyotp.html', context)

            else:
                transfer.status = 'pending'
                transfer.save()
                context = {
                    'msg': 'Your transaction has been verified and placed.View it in transfer history.',
                    'color': 'green',
                    'text_color': 'white',
                    'histories': TransferRequest.objects.all().order_by('-date'),
                }
                return render(request, 'banking/history.html', context)
        else:
            context = {
                'msg': form.errors,
                'color': 'yellow', }
            return render(request, 'banking/verifyotp.html', context)


class DashboardView(LoginRequiredMixin, View):
    login_url = '/sign-in'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'banking/dashboard.html')


class HistorySearchView(LoginRequiredMixin, View):
    login_url = '/sign-in'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        query = str(request.POST.get('query', ''))
        if query == '':
            context = {
                'msg': 'The search query you entered is invalid',
                'color': 'blue',
            }
            return redirect(request.path, context=context)
        else:
            match_by_status = list(
                TransferRequest.objects.all().filter(status__icontains=query))
            match_by_account_number = list(
                TransferRequest.objects.all().filter(account_number=query))

            matches = match_by_account_number + match_by_status

            # if query.:
            #     matches += list(TransferRequest.objects.all().filter(tx_id=query))

            if query.isdigit():
                matches += list(TransferRequest.objects.all().filter(amount=int(query)))

            context = {
                'matches': matches,
                'search': True,
                'count': len(matches),
            }

            return render(request, 'banking/historysearch.html', context)

            # pass


class TransferView(LoginRequiredMixin, View):
    login_url = '/sign-in'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'banking/transfer.html')

    def post(self, request):
        form = None
        if request.POST.get('transfer_type') == 'local':
            form = LocalTransferForm(request.POST)
        elif request.POST.get('transfer_type') == 'Intl':
            form = IntlTransferForm(request.POST)
        else:
            return HttpResponse(status=400, content='Transfer Type was not specified')

        if form.is_valid():
            new_transfer_request = TransferRequest(
                user=request.user,
                account_number=form.cleaned_data['account_number'],
                amount=form.cleaned_data['amount'],
                transfer_type=request.POST.get('transfer_type'),
                bank_name=form.cleaned_data.get('bank_name', ''),
                bank_address=form.cleaned_data.get('bank_address', ''),
                bank_swift=form.cleaned_data.get('bank_swift', ''),
                bank_iban=form.cleaned_data.get('bank_iban', ''),
                # status= 'unverified',

            )
            new_transfer_request.save()
            # context = {
            #     'msg': 'Your transfer request has been succesfully placed.Check the progress on the transfer history',
            #     'color': 'green',
            # }
            otp = OTP.objects.create(
                user=request.user,
                timeline_in_minutes=15,
            )
            print("\n\nOTP : ", otp.code, '\n\n')
            otp.send()

            return redirect('/verify-with-otp/{0}/'.format(new_transfer_request.tx_id))

        else:
            context = {
                'msg': str(form.errors),
                'color': 'yellow',
            }
            return render(request, 'banking/transfer.html', context)


class HistoryView(LoginRequiredMixin, View):
    login_url = '/sign-in'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        transfers = request.user.transfer_requests.order_by('-date').all()
        context = {
            'histories': transfers
        }

        return render(request, 'banking/history.html', context)


class SignInView(View):
    def get(self, request):
        return render(request, 'banking/signin.html')

    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is None:
                context = {
                    'msg': 'Invalid credentials',
                    'color': 'red',
                }
                return render(request, 'banking/signin.html', context)
            else:
                login(request, user)
                destination = request.GET.get('redirect_to','/dashboard')
                return redirect(destination)

            # return render(request, 'banking/')
        else:
            context = {
                'msg': form.errors,
                'color': 'yellow',
            }
            return render(request, 'banking/signin.html', context)
