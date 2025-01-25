import torch
from tqdm import tqdm
import os
from torch import nn
from torch.utils.tensorboard import SummaryWriter


def test(model, testloader, criterion):

    model.eval()  # 将模型设置为评估模式
    criterion = criterion.cuda()
    
    sum_loss = 0

    loop = enumerate(testloader)

    with torch.no_grad():  
        for i, (data, targets) in (loop):
            # Get data to cuda if possible
            # forward
            scores = model(data)
            loss = criterion(scores, targets)

            sum_loss += loss.item()
    
    return sum_loss / (testloader.__len__())


## 可以考虑保存优化器
# 不实现gt 与 x 进行cuda(), 直接在Dataset中对gt进行.cuda()以实现更灵活的模型
# def train(model, criterion, optimizer, trainloader, epochs, testloader, testEpoch, modelSavedPath='../data/model/', scheduler=None,
#            resume=False, checkpoint_path=None):

#     if not os.path.exists(modelSavedPath):
#         os.makedirs(modelSavedPath)
#         print(f'{modelSavedPath} mkdir success')


#     model = model.cuda()
#     if resume and checkpoint_path is not None and os.path.isfile(checkpoint_path):
#         print(f"Loading checkpoint from {checkpoint_path}")
#         checkpoint = torch.load(checkpoint_path)
#         model.load_state_dict(checkpoint['model_state_dict'])

#         optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

#         start_epoch = checkpoint['epoch'] + 1
#         test_min_loss = checkpoint['test_min_loss']

#         if scheduler != None and 'scheduler_state_dict' in checkpoint:
#             scheduler.load_state_dict(checkpoint['scheduler_state_dict'])

#         print(f"Resumed training from epoch {start_epoch}")
#     elif resume and checkpoint_path is not None and not os.path.isfile(checkpoint_path):
#         print('No checkpoint found, training from scratch')

#     criterion = criterion.cuda()

#     test_min_loss = 9e9

#     for epoch in range(epochs):

#         loop = tqdm(enumerate(trainloader), total=(len(trainloader)))
#         loop.set_description(f'Epoch [{epoch}/{epochs}]')

#         sum_loss = 0
#         count = 0

#         for i, (data, targets) in loop:
#             # forward
#             scores = model(data)
#             loss = criterion(scores, targets)

#             sum_loss += loss.item()
#             count += 1

#             # backward
#             optimizer.zero_grad()
#             loss.backward()

#             # gardient descent or adam step
#             optimizer.step()

#         print(f'train loss:{sum_loss / count}')

#         if epoch % testEpoch == 0:

#             test_loss = test(model, testloader, criterion)

#             print(f'test loss:{test_loss}')

#             if test_loss < test_min_loss:
#                 test_min_loss = test_loss

#                 torch.save(model.state_dict(), os.path.join(modelSavedPath, 'best_model.pkl'))
#                 print(f'{epoch}\'s model have saved to best_model.pkl')

#         # test后再scheduler
#         if scheduler != None:
#             scheduler.step()
            
#     torch.save(model.state_dict(), os.path.join(modelSavedPath, f'{epoch}_model.pkl'))


def train(model, criterion, optimizer, trainloader, epochs, testloader, testEpoch, modelSavedPath='../data/model/', 
          scheduler=None, resume=False, checkpoint_path=None):

    if not os.path.exists(modelSavedPath):
        os.makedirs(modelSavedPath)
        print(f'{modelSavedPath} mkdir success')

    start_epoch = 0
    test_min_loss = 9e9

    if resume and checkpoint_path is not None and os.path.isfile(checkpoint_path):
        print(f"Loading checkpoint from {checkpoint_path}")
        checkpoint = torch.load(checkpoint_path)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        start_epoch = checkpoint['epoch'] + 1
        test_min_loss = checkpoint['test_min_loss']
        if scheduler is not None and 'scheduler_state_dict' in checkpoint:
            scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
        print(f"Resumed training from epoch {start_epoch}")

    model = model.cuda()
    criterion = criterion.cuda()

    for epoch in range(start_epoch, epochs):

        loop = tqdm(enumerate(trainloader), total=(len(trainloader)))
        loop.set_description(f'Epoch [{epoch}/{epochs}]')

        sum_loss = 0
        count = 0

        for i, (data, targets) in loop:
            # forward
            scores = model(data)
            loss = criterion(scores, targets)

            sum_loss += loss.item()
            count += 1

            # backward
            optimizer.zero_grad()
            loss.backward()

            # gradient descent or adam step
            optimizer.step()

        print(f'train loss:{sum_loss / count}')

        if epoch % testEpoch == 0:

            test_loss = test(model, testloader, criterion)

            print(f'test loss:{test_loss}')

            if test_loss < test_min_loss:
                test_min_loss = test_loss
                # Save checkpoint
                checkpoint = {
                    'epoch': epoch,
                    'model_state_dict': model.state_dict(),
                    'optimizer_state_dict': optimizer.state_dict(),
                    'test_min_loss': test_min_loss
                }
                if scheduler is not None:
                    checkpoint['scheduler_state_dict'] = scheduler.state_dict()
                torch.save(checkpoint, os.path.join(modelSavedPath, 'checkpoint.pth'))
                print(f'Checkpoint saved at epoch {epoch}')

        # test后再scheduler
        if scheduler is not None:
            scheduler.step()
    checkpoint = {
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'test_min_loss': test_min_loss
    }
    if scheduler is not None:
        checkpoint['scheduler_state_dict'] = scheduler.state_dict()
    torch.save(checkpoint, os.path.join(modelSavedPath, 'checkpoint.pth'))
    print(f'Checkpoint saved at epoch {epoch}')

    torch.save(model.state_dict(), os.path.join(modelSavedPath, f'{epoch}_model.pkl'))