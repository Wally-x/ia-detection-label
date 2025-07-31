if __name__ == "__main__":
    import torch
    import torchvision
    import optuna
    import albumentations

    print("Torch:", torch.__version__)
    print("CUDA dispo ?", torch.cuda.is_available())