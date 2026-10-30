from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import Forms
from .models import Message


def Contact(request):
    if request.method == 'POST':
        form = Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/?success=1#contact')
    else:
        form = Forms()

    return render(request, 'adminp/home.html', {'form': form})


@login_required
def message_list(request):
    messages = Message.objects.order_by('-created_at')
    return render(request, 'adminp/message.html', {'messages': messages})

@login_required
@require_POST
def del_message(request,pk):
    message=get_object_or_404(Message,id=pk)
    message.delete()
    return redirect('message_list')
