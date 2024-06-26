import torch
from misc import colorize

class DepthEstimationModel:
    def __init__(self) -> None:
        self.device=self._get_device()
        self.model=self._initialize_model(model_repo="isl-org/ZoeDepth",model_name="Zoed_N").to(self.device)

    def _get_device(self):
        return 'cuda' if torch.cuda.is_available() else "cpu"
    def _initialize_model(self,model_repo="isl-org/ZoeDepth",model_name="Zoed_N"):
        torch.hub.help("intel-isl/MiDaS", "DPT_BEiT_L_384", force_reload=True)  
        model=torch.hub(model_repo,model_name,pretrained=True,skip_validation=False)
        model.eval()
        print("model initialized")
        return model
        
