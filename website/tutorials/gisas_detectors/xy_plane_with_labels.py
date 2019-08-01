import ROOT


def hold_root_graphics():
    """
    Holds ROOT graphics while listening to ctr-C event
    """
    Interrupt = False
    while not Interrupt:
        Interrupt = ROOT.gSystem.ProcessEvents()
        ROOT.gSystem.Sleep(10)




nbinx = 10
xmin = 0.0
xmax = 200.0
dx = (xmax-xmin)/nbinx
nbiny = 9
ymin = 0.0
ymax = 180.0
dy = (ymax-ymin)/nbiny
print dx,dy


c1 = ROOT.TCanvas("c1","c1",640, 640)
# c1 = ROOT.TCanvas("c1","c1",2000, 1800)
c1.Draw()
c1.cd()
ROOT.gPad.SetLeftMargin(0.1)
ROOT.gPad.SetRightMargin(0.1)
ROOT.gPad.SetTopMargin(0.1)
ROOT.gPad.SetBottomMargin(0.1)
# ROOT.gPad.SetFillColor(19)


h2 = ROOT.TH2D("h2","h2", nbinx, xmin, xmax, nbiny, ymin, ymax)
h2.SetTitle("")
h2.SetStats(0)

h2.GetXaxis().SetTitle("X, mm")
h2.GetXaxis().SetTitleSize(0.04)
h2.GetXaxis().SetTitleOffset(1.1)

h2.GetYaxis().SetTitle("Y, mm")
h2.GetYaxis().SetTitleSize(0.04)
h2.GetYaxis().SetTitleOffset(1.2)

h2.GetYaxis().SetNdivisions(508)
h2.Draw()

line = ROOT.TLine()
line.SetLineStyle(2)
for nx in range(0, nbinx):
    line.DrawLine(xmin + dx*nx, ymin, xmin + dx*nx, ymax)

for ny in range(0, nbiny):
    line.DrawLine(xmin, ymin + dy*ny, xmax, ymin + dy*ny)

marker = ROOT.TMarker()
marker.SetMarkerStyle(20)
marker.SetMarkerColor(ROOT.kBlue)
for nx in range(0, nbinx):
    x = xmin + dx/2. + dx*nx
    for ny in range(0, nbiny):
        y = ymin + dy/2. + dy*ny
        marker.DrawMarker(x, y)



c1.Modified()
c1.Update()

hold_root_graphics()


