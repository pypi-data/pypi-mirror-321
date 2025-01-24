import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { IStatusBar } from '@jupyterlab/statusbar';
import { RecoveryModeWidget } from '../../widgets/RecoveryModeWidget';

const RecoveryModePlugin: JupyterFrontEndPlugin<void> = {
  id: 'recoverymode:plugin',
  autoStart: true,
  requires: [IStatusBar],
  activate: async (app: JupyterFrontEnd, statusBar: IStatusBar) => {
    const isRecoveryMode = await getRecoveryModeStatus();
    if (isRecoveryMode) {
      const widget = new RecoveryModeWidget();
      statusBar.registerStatusItem('recoverymode:statusbar', {
        align: 'right',
        item: widget,
        rank: 1000,
      });
    }
  },
};

/**
 * Fetches the recovery mode status from the Jupyter server API.
 * @returns A promise that resolves to `true` if recovery mode is enabled, `false` otherwise.
 */
async function getRecoveryModeStatus(): Promise<boolean> {
  try {
    const response = await fetch('/aws/sagemaker/api/recovery-mode', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      return false;
    }

    const data = await response.json();
    return data.sagemakerRecoveryMode === 'true';
  } catch (error) {
    return false;
  }
}

export { RecoveryModePlugin };
